from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.gis.geos import GEOSGeometry
from django.core.exceptions import ObjectDoesNotExist
from madrona.features.models import Feature
from madrona.features import get_feature_by_uid
from madrona.common.utils import LargestPolyFromMulti
from scenarios.models import GridCell
from drawing.models import *
from drawing.ofr_manipulators import clip_to_grid
from json import dumps


'''
'''
def get_drawings(request):
    json = []
    if request.user.is_authenticated:
        drawings = AOI.objects.filter(user=request.user).order_by('date_created')
    else:
        drawings = AOI.objects.filter(user=None)
    for drawing in drawings:
        sharing_groups = [group.name for group in drawing.sharing_groups.all()]
        json.append({
            'id': drawing.id,
            'uid': drawing.uid,
            'name': drawing.name,
            'description': drawing.description,
            'attributes': drawing.serialize_attributes,
            'sharing_groups': sharing_groups
        })

    shared_drawings = AOI.objects.shared_with_user(request.user)
    for drawing in shared_drawings:
        if drawing not in drawings:
            username = drawing.user.username
            actual_name = drawing.user.first_name + ' ' + drawing.user.last_name
            json.append({
                'id': drawing.id,
                'uid': drawing.uid,
                'name': drawing.name,
                'description': drawing.description,
                'attributes': drawing.serialize_attributes,
                'shared': True,
                'shared_by_username': username,
                'shared_by_name': actual_name
            })

    return HttpResponse(dumps(json))

'''
'''
def delete_drawing(request, uid):
    try:
        drawing_obj = get_feature_by_uid(uid)
    except ObjectDoesNotExist:
        raise Http404
    except AttributeError:
        raise Http404

    #check permissions
    viewable, response = drawing_obj.is_viewable(request.user)
    if not viewable:
        return response

    drawing_obj.delete()

    return HttpResponse("", status=200)

'''
'''
def get_clipped_shape(request):
    zero = .01

    if not (request.POST and request.POST['target_shape']):
        return HTTPResponse("No shape submitted", status=400)

    target_shape = request.POST['target_shape']
    geom = GEOSGeometry(target_shape, srid=3857)

    clipped_shape = clip_to_grid(geom)

    # return new_shape['geometry__union']
    if clipped_shape and clipped_shape.area >= zero: #there was overlap
        largest_poly = LargestPolyFromMulti(clipped_shape)
        wkt = largest_poly.wkt
        return HttpResponse(dumps({"clipped_wkt": wkt}), status=200)
    else:
        return HttpResponse("Submitted Shape is outside Grid Cell Boundaries (no overlap).", status=400)

    # return HttpResponse(dumps({"clipped_wkt": wkt}), status=200)

'''
'''
def aoi_analysis(request, aoi_id):
    from aoi_analysis import display_aoi_analysis
    aoi_obj = get_object_or_404(AOI, pk=aoi_id)
    #check permissions
    viewable, response = aoi_obj.is_viewable(request.user)
    if not viewable:
        return response
    return display_aoi_analysis(request, aoi_obj)
    # Create your views here.

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

def get_report_data(request, uid=None):
        try:
            scenario_obj = get_feature_by_uid(uid)
            #check permissions
            viewable, response = scenario_obj.is_viewable(request.user)
            if not viewable:
                return response

            context = scenario_obj.serialize_attributes
            context['title'] = 'Strategy Report: %s' % scenario_obj.name
        except AttributeError as e:
            attributes = []
            context = {'event': 'click', 'attributes': []}
            if request.method == 'POST':
                if 'parameter' in request.POST.dict().keys():
                    data = eval(request.POST.get('parameter'))
                    for item in data:
                        attributes.append({
                            'title': item['display'],
                            'data': item['data'],
                        })
                else:
                    data = request.POST.dict()
                    for key in data.keys():
                        attributes.append({
                            'title': key,
                            'data': data[key]
                        })
                context['attributes'] = attributes

        except Exception as e:
            raise Http404

        return context

def get_report_html(request, uid=None, template='aoi/reports/report.html'):
    context = get_report_data(request, uid)

    return render(request, template, context)

def get_report_print(request, uid=None, template='aoi/reports/report_print.html'):
    context = get_report_data(request, uid)
    context['title'] = 'Strategy Report'
    context['description'] = None

    for attr in context['attributes']:
        if attr['title'] == 'layer':
            context['title'] = "Strategy Report: %s" % attr['data']
        if attr['title'] == 'Description':
            context['description'] = attr['data']

    return render(request, template, context)

'''
'''
def get_geometry_orig(request, uid):
    try:
        scenario_obj = get_feature_by_uid(uid)
        wkt = scenario_obj.geometry_orig.wkt
    except Scenario.DoesNotExist:
        raise Http404

    #check permissions
    viewable, response = scenario_obj.is_viewable(request.user)
    if not viewable:
        return response

    return HttpResponse(dumps({"geometry_orig": wkt}), status=200)

'''
'''
# def wind_analysis(request, wind_id):
#     from wind_analysis import display_wind_analysis
#     wind_obj = get_object_or_404(WindEnergySite, pk=wind_id)
#     #check permissions
#     viewable, response = wind_obj.is_viewable(request.user)
#     if not viewable:
#         return response
#     return display_wind_analysis(request, wind_obj)
#     # Create your views here.

'''
'''
def get_csv(request, uid, download=True):
    import csv
    if 'drawing_aoi_' in uid:
        aoi_id = str(int(''.join([x for x in filter(str.isdigit, str(uid))])))
    else:
        aoi_id = int(uid)
    # aoi_id = int(request.POST['id'])
    try:
        drawing = AOI.objects.get(id=aoi_id)
    except:
        return HttpResponse(
            dumps(
                {
                    'message': 'Could not find drawing with id = %d' % aoi_id
                }
            ),
            status=500
        )
    filename = '%s_%d_drawing.csv' % (drawing.name, drawing.id)
    summaryReports = drawing.summary_reports({'list_style':'list'})
    if download:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s' % (filename)
        writer = csv.writer(response)
    else:
        import settings
        csv_file = open('%s%s' % (settings.PUBLIC_CSV_DIR,filename), 'w')
        writer = csv.writer(csv_file)
    headers = ['Name']
    report_data = {'Name':drawing.name}
    max_row_count = 2   #for disclaimer
    for attribute in summaryReports:
        headers.append(attribute['title'])
        if type(attribute['data']) is (list or tuple):
            attr_length = len(attribute['data'])
            if attr_length > max_row_count:
                max_row_count = attr_length
        report_data[attribute['title']] = attribute['data']

    # Move Observed Species to end of list to be next to disclaimer
    observed = 'Observed Wildlife'
    if observed in headers:
        headers.insert(len(headers)-1, headers.pop(headers.index(observed)))
    headers.append('Disclaimer')
    report_data['Disclaimer'] = [
    "Data used to generate this report has been summarized.",
    "See http://dfw.state.or.us/maps/compass/reportingtool.asp"
    ]
    writer.writerow(headers)
    for index in range(max_row_count):
        row = []
        for header in headers:
            data = report_data[header]
            if type(data) is (list or tuple):
                if index+1 > len(data):
                    row.append("")
                else:
                    row.append(data[index])
            else:
                if index < 1:
                    row.append(data)
                else:
                    row.append("")
        writer.writerow(row)

    if download:
        return response
    else:
        csv_file.close()
        return '%s%s' % (settings.PUBLIC_CSV_URL,filename)
