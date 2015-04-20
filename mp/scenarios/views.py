from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.views.decorators.cache import cache_page
from madrona.features.models import Feature
from madrona.features import get_feature_by_uid
from general.utils import meters_to_feet
from models import *
from simplejson import dumps
from django.contrib.gis.db.models.aggregates import Union


'''
'''
def sdc_analysis(request, sdc_id):
    from sdc_analysis import display_sdc_analysis
    sdc_obj = get_object_or_404(Scenario, pk=sdc_id)
    #check permissions
    viewable, response = sdc_obj.is_viewable(request.user)
    if not viewable:
        return response
    return display_sdc_analysis(request, sdc_obj)

'''
'''
def copy_design(request, uid):
    try:
        design_obj = get_feature_by_uid(uid)
    except Feature.DoesNotExist:
        raise Http404

    #check permissions
    viewable, response = design_obj.is_viewable(request.user)
    if not viewable:
        return response

    design_obj.pk = None
    design_obj.user = request.user
    design_obj.save()

    json = []
    json.append({
        'id': design_obj.id,
        'uid': design_obj.uid,
        'name': design_obj.name,
        'description': design_obj.description,
        'attributes': design_obj.serialize_attributes
    })

    return HttpResponse(dumps(json), status=200)

'''
'''
def delete_design(request, uid):
    try:
        design_obj = get_feature_by_uid(uid)
    except Feature.DoesNotExist:
        raise Http404

    #check permissions
    viewable, response = design_obj.is_viewable(request.user)
    if not viewable:
        return response

    design_obj.delete()
    #design_obj.active = False
    #design_obj.save(rerun=False)

    return HttpResponse("", status=200)

'''
'''
def get_scenarios(request):
    json = []

    scenarios = Scenario.objects.filter(user=request.user, active=True).order_by('date_created')
    for scenario in scenarios:
        sharing_groups = [group.name for group in scenario.sharing_groups.all()]
        json.append({
            'id': scenario.id,
            'uid': scenario.uid,
            'name': scenario.name,
            'description': scenario.description,
            'attributes': scenario.serialize_attributes,
            'sharing_groups': sharing_groups
        })

    shared_scenarios = Scenario.objects.shared_with_user(request.user)
    for scenario in shared_scenarios:
        if scenario.active and scenario not in scenarios:
            username = scenario.user.username
            actual_name = scenario.user.first_name + ' ' + scenario.user.last_name
            json.append({
                'id': scenario.id,
                'uid': scenario.uid,
                'name': scenario.name,
                'description': scenario.description,
                'attributes': scenario.serialize_attributes,
                'shared': True,
                'shared_by_username': username,
                'shared_by_name': actual_name
            })

    return HttpResponse(dumps(json))

'''
'''
def get_selections(request):
    json = []
    selections = LeaseBlockSelection.objects.filter(user=request.user).order_by('date_created')
    for selection in selections:
        sharing_groups = [group.name for group in selection.sharing_groups.all()]
        json.append({
            'id': selection.id,
            'uid': selection.uid,
            'name': selection.name,
            'description': selection.description,
            'attributes': selection.serialize_attributes,
            'sharing_groups': sharing_groups
        })

    shared_selections = LeaseBlockSelection.objects.shared_with_user(request.user)
    for selection in shared_selections:
        if selection not in selections:
            username = selection.user.username
            actual_name = selection.user.first_name + ' ' + selection.user.last_name
            json.append({
                'id': selection.id,
                'uid': selection.uid,
                'name': selection.name,
                'description': selection.description,
                'attributes': selection.serialize_attributes,
                'shared': True,
                'shared_by_username': username,
                'shared_by_name': actual_name
            })

    return HttpResponse(dumps(json))

'''
'''
def get_leaseblock_features(request):
    from madrona.common.jsonutils import get_properties_json, get_feature_json, srid_to_urn, srid_to_proj
    srid = settings.GEOJSON_SRID
    leaseblock_ids = request.GET.getlist('leaseblock_ids[]')
    leaseblocks = LeaseBlock.objects.filter(prot_numb__in=leaseblock_ids)
    feature_jsons = []
    for leaseblock in leaseblocks:
        try:
            geom = leaseblock.geometry.transform(srid, clone=True).json
        except:
            srid = settings.GEOJSON_SRID_BACKUP
            geom = leaseblock.geometry.transform(srid, clone=True).json
        feature_jsons.append(get_feature_json(geom, json.dumps('')))#json.dumps(props)))
        #feature_jsons.append(leaseblock.geometry.transform(srid, clone=True).json)
        '''
        geojson = """{
          "type": "Feature",
          "geometry": %s,
          "properties": {}
        }""" %leaseblock.geometry.transform(settings.GEOJSON_SRID, clone=True).json
        '''
        #json.append({'type': "Feature", 'geometry': leaseblock.geometry.geojson, 'properties': {}})
    #return HttpResponse(dumps(json[0]))
    geojson = """{
      "type": "FeatureCollection",
      "crs": { "type": "name", "properties": {"name": "%s"}},
      "features": [
      %s
      ]
    }""" % (srid_to_urn(srid), ', \n'.join(feature_jsons),)
    return HttpResponse(geojson)

'''
'''
def get_attributes(request, uid):
    try:
        scenario_obj = get_feature_by_uid(uid)
    except Scenario.DoesNotExist:
        raise Http404

    #check permissions
    viewable, response = scenario_obj.is_viewable(request.user)
    if not viewable:
        return response

    return HttpResponse(dumps(scenario_obj.serialize_attributes))

'''
'''
def get_sharing_groups(request):
    from madrona.features import user_sharing_groups
    from functools import cmp_to_key
    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    json = []
    sharing_groups = user_sharing_groups(request.user)
    for group in sharing_groups:
        members = []
        for user in group.user_set.all():
            if user.first_name.replace(' ', '') != '' and user.last_name.replace(' ', '') != '':
                members.append(user.first_name + ' ' + user.last_name)
            else:
                members.append(user.username)
        sorted_members = sorted(members, key=cmp_to_key(locale.strcoll))
        json.append({
            'group_name': group.name,
            'group_slug': slugify(group.name)+'-sharing',
            'members': sorted_members
        })
    return HttpResponse(dumps(json))

'''
'''
def share_design(request):
    from django.contrib.auth.models import Group
    group_names = request.POST.getlist('groups[]')
    design_uid = request.POST['scenario']
    design = get_feature_by_uid(design_uid)
    viewable, response = design.is_viewable(request.user)
    if not viewable:
        return response
    #remove previously shared with groups, before sharing with new list
    design.share_with(None)
    groups = []
    for group_name in group_names:
        groups.append(Group.objects.get(name=group_name))
    design.share_with(groups, append=False)
    return HttpResponse("", status=200)

'''
'''
def run_filter_query(filters):
    # TODO: This would be nicer if it generically knew how to filter fields
    # by name, and what kinds of filters they were. For now, hard code.
    query = GridCell.objects.all()

    if 'acropora_pa' in filters.keys() and filters['acropora_pa']:
        query = query.filter(acropora_pa=filters['acropora_pa_input'])

    # Special case, anchor_desc is not exclusive category but an ordinal category
    if 'anchor_desc' in filters.keys() and filters['anchor_desc']:
        levels = ['Low', 'Medium', 'High', 'Very High']
        levelsin = levels[levels.index(filters['anchor_desc_input']):]
        query = query.filter(anchor_desc__in=levelsin)

    if 'anchorage' in filters.keys() and filters['anchorage']:
        query = query.filter(anchorage=filters['anchorage_input'])

    if 'boat_use' in filters.keys() and filters['boat_use']:
        query = query.filter(boat_use__gte=filters['boat_use_min'])
        query = query.filter(boat_use__lte=filters['boat_use_max'])

    if 'coral_bleach' in filters.keys() and filters['coral_bleach']:
        query = query.filter(coral_bleach__gte=filters['coral_bleach_min'])
        query = query.filter(coral_bleach__lte=filters['coral_bleach_max'])

    if 'coral_cover' in filters.keys() and filters['coral_cover']:
        query = query.filter(coral_cover__gte=filters['coral_cover_min'])
        query = query.filter(coral_cover__lte=filters['coral_cover_max'])

    if 'coral_density' in filters.keys() and filters['coral_density']:
        query = query.filter(coral_density__gte=filters['coral_density_min'])
        query = query.filter(coral_density__lte=filters['coral_density_max'])

    if 'coral_disease' in filters.keys() and filters['coral_disease']:
        query = query.filter(coral_disease__gte=filters['coral_disease_min'])
        query = query.filter(coral_disease__lte=filters['coral_disease_max'])

    if 'coral_resilience' in filters.keys() and filters['coral_resilience']:
        query = query.filter(coral_resilience__gte=filters['coral_resilience_min'])
        query = query.filter(coral_resilience__lte=filters['coral_resilience_max'])

    if 'coral_richness' in filters.keys() and filters['coral_richness']:
        query = query.filter(coral_richness__gte=filters['coral_richness_min'])
        query = query.filter(coral_richness__lte=filters['coral_richness_max'])

    if 'coral_soft' in filters.keys() and filters['coral_soft']:
        query = query.filter(coral_soft__gte=filters['coral_soft_min'])
        query = query.filter(coral_soft__lte=filters['coral_soft_max'])

    if 'depth_mean' in filters.keys() and filters['depth_mean']:
        query = query.filter(depth_mean__gte=filters['depth_mean_min'])
        query = query.filter(depth_mean__lte=filters['depth_mean_max'])

    if 'divefish_overlap' in filters.keys() and filters['divefish_overlap']:
        query = query.filter(divefish_overlap__gte=filters['divefish_overlap_min'])
        query = query.filter(divefish_overlap__lte=filters['divefish_overlap_max'])

    if 'extdive_use' in filters.keys() and filters['extdive_use']:
        query = query.filter(extdive_use__gte=filters['extdive_use_min'])
        query = query.filter(extdive_use__lte=filters['extdive_use_max'])

    if 'impacted' in filters.keys() and filters['impacted']:
        query = query.filter(impacted=filters['impacted_input'])

    if 'injury_site' in filters.keys() and filters['injury_site']:
        query = query.filter(injury_site=filters['injury_site_input'])

    if 'inlet_distance' in filters.keys() and filters['inlet_distance']:
        query = query.filter(inlet_distance__gte=filters['inlet_distance_min'])
        query = query.filter(inlet_distance__lte=filters['inlet_distance_max'])

    if 'large_live_coral' in filters.keys() and filters['large_live_coral']:
        query = query.filter(large_live_coral=filters['large_live_coral_input'])

    if 'mooring_buoy' in filters.keys() and filters['mooring_buoy']:
        query = query.filter(mooring_buoy=filters['mooring_buoy_input'])

    # Special case, mooring_desc is not exclusive category but an ordinal range
    if 'mooring_desc' in filters.keys() and filters['mooring_desc']:
        levels = ['Low', 'Medium', 'High', 'Very High']
        levelsin = levels[levels.index(filters['mooring_desc_input']):]
        query = query.filter(mooring_desc__in=levelsin)

    if 'outfall_distance' in filters.keys() and filters['outfall_distance']:
        query = query.filter(outfall_distance__gte=filters['outfall_distance_min'])
        query = query.filter(outfall_distance__lte=filters['outfall_distance_max'])

    if 'pier_distance' in filters.keys() and filters['pier_distance']:
        query = query.filter(pier_distance__gte=filters['pier_distance_min'])
        query = query.filter(pier_distance__lte=filters['pier_distance_max'])

    if 'pillar_presence'in filters.keys() and filters['pillar_presence']:
        query = query.filter(pillar_presence=filters['pillar_presence_input'])

    if 'prcnt_art' in filters.keys() and filters['prcnt_art']:
        query = query.filter(prcnt_art__gte=filters['prcnt_art_min'])
        query = query.filter(prcnt_art__lte=filters['prcnt_art_max'])

    if 'prcnt_reef' in filters.keys() and filters['prcnt_reef']:
        query = query.filter(prcnt_reef__gte=filters['prcnt_reef_min'])
        query = query.filter(prcnt_reef__lte=filters['prcnt_reef_max'])

    if 'prcnt_sand' in filters.keys() and filters['prcnt_sand']:
        query = query.filter(prcnt_sand__gte=filters['prcnt_sand_min'])
        query = query.filter(prcnt_sand__lte=filters['prcnt_sand_max'])

    if 'prcnt_sg' in filters.keys() and filters['prcnt_sg']:
        query = query.filter(prcnt_sg__gte=filters['prcnt_sg_min'])
        query = query.filter(prcnt_sg__lte=filters['prcnt_sg_max'])

    if 'reccom_fish' in filters.keys() and filters['reccom_fish']:
        query = query.filter(reccom_fish__gte=filters['reccom_fish_min'])
        query = query.filter(reccom_fish__lte=filters['reccom_fish_max'])

    if 'recfish_use' in filters.keys() and filters['recfish_use']:
        query = query.filter(recfish_use__gte=filters['recfish_use_min'])
        query = query.filter(recfish_use__lte=filters['recfish_use_max'])

    if 'reef_fish_density' in filters.keys() and filters['reef_fish_density']:
        query = query.filter(reef_fish_density__gte=filters['reef_fish_density_min'])
        query = query.filter(reef_fish_density__lte=filters['reef_fish_density_max'])

    if 'reef_fish_richness' in filters.keys() and filters['reef_fish_richness']:
        query = query.filter(reef_fish_richness__gte=filters['reef_fish_richness_min'])
        query = query.filter(reef_fish_richness__lte=filters['reef_fish_richness_max'])

    if 'scuba_use' in filters.keys() and filters['scuba_use']:
        query = query.filter(scuba_use__gte=filters['scuba_use_min'])
        query = query.filter(scuba_use__lte=filters['scuba_use_max'])

    if 'shore_distance' in filters.keys() and filters['shore_distance']:
        query = query.filter(shore_distance__gte=filters['shore_distance_min'])
        query = query.filter(shore_distance__lte=filters['shore_distance_max'])

    if 'spear_use' in filters.keys() and filters['spear_use']:
        query = query.filter(spear_use__gte=filters['spear_use_min'])
        query = query.filter(spear_use__lte=filters['spear_use_max'])

    if 'sponge' in filters.keys() and filters['sponge']:
        query = query.filter(sponge__gte=filters['sponge_min'])
        query = query.filter(sponge__lte=filters['sponge_max'])

    if 'total_use' in filters.keys() and filters['total_use']:
        query = query.filter(total_use__gte=filters['total_use_min'])
        query = query.filter(total_use__lte=filters['total_use_max'])

    if 'watersport_use' in filters.keys() and filters['watersport_use']:
        query = query.filter(watersport_use__gte=filters['watersport_use_min'])
        query = query.filter(watersport_use__lte=filters['watersport_use_max'])

    return query

'''
'''
@cache_page(60 * 60) # 1 hour of caching
def get_filter_count(request):
    filter_dict = dict(request.GET.iteritems())
    query = run_filter_query(filter_dict)
    return HttpResponse(query.count(), status=200)


@cache_page(60 * 60)  # 1 hour of caching
def get_filter_results(request):
    filter_dict = dict(request.GET.iteritems())
    query = run_filter_query(filter_dict)

    json = []
    count = query.count()
    if count == 0:
        json = [{
            'count': 0,
            'wkt': None
        }]
    else:

        union_agg = query.aggregate(Union('geometry'))
        dissolved_geom = union_agg['geometry__union']
        if not dissolved_geom:
            raise Exception("No lease blocks available with the current filters.")
        json = [{
            'count': count,
            'wkt': dissolved_geom.wkt
        }]

    # return # of grid cells and dissolved geometry in geojson
    return HttpResponse(dumps(json))

'''
'''
#@cache_page(60 * 60 * 24, key_prefix="scenarios_get_leaseblocks")
def get_leaseblocks(request):
    json = []
    for grid_cell in GridCell.objects.all():
        json.append({
            'id': grid_cell.id,
            'shore_distance': grid_cell.shore_distance,
            'pier_distance': grid_cell.pier_distance,
            'inlet_distance': grid_cell.inlet_distance,
            'outfall_distance': grid_cell.outfall_distance,
            'fish_richness': grid_cell.fish_richness,
            'coral_richness': grid_cell.coral_richness,
            'coral_density': grid_cell.coral_density,
            # 'coral_size': grid_cell.coral_size
        })
    return HttpResponse(dumps(json))

