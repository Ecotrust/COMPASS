# coding: utf-8

import os
import time
import json
from picklefield import PickledObjectField
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.html import escape
from madrona.common.utils import asKml
from madrona.common.jsonutils import get_properties_json, get_feature_json
from madrona.features import register
from madrona.analysistools.models import Analysis
from general.utils import miles_to_meters, feet_to_meters, meters_to_feet, mph_to_mps, mps_to_mph, format_precision
from django.contrib.gis.geos import MultiPolygon
from django.contrib.gis.db.models.aggregates import Union
from django.forms.models import model_to_dict


@register
class Scenario(Analysis):

    acropora_pa = models.BooleanField()
    acropora_pa_input = models.TextField(null=True, blank=True)

    anchor_desc = models.BooleanField()
    anchor_desc_input = models.TextField(null=True, blank=True)

    anchorage = models.BooleanField()
    anchorage_input = models.TextField(null=True, blank=True)

    boat_use = models.BooleanField()
    boat_use_min = models.FloatField(null=True, blank=True)
    boat_use_max = models.FloatField(null=True, blank=True)

    coral_bleach = models.BooleanField()
    coral_bleach_min = models.FloatField(null=True, blank=True)
    coral_bleach_max = models.FloatField(null=True, blank=True)

    coral_cover = models.BooleanField()
    coral_cover_min = models.FloatField(null=True, blank=True)
    coral_cover_max = models.FloatField(null=True, blank=True)

    coral_density = models.BooleanField()
    coral_density_min = models.FloatField(null=True, blank=True)
    coral_density_max = models.FloatField(null=True, blank=True)

    coral_disease = models.BooleanField()
    coral_disease_min = models.FloatField(null=True, blank=True)
    coral_disease_max = models.FloatField(null=True, blank=True)

    coral_resilience = models.BooleanField()
    coral_resilience_min = models.FloatField(null=True, blank=True)
    coral_resilience_max = models.FloatField(null=True, blank=True)

    coral_richness = models.BooleanField()
    coral_richness_min = models.FloatField(null=True, blank=True)
    coral_richness_max = models.FloatField(null=True, blank=True)

    coral_soft = models.BooleanField()
    coral_soft_min = models.FloatField(null=True, blank=True)
    coral_soft_max = models.FloatField(null=True, blank=True)

    depth_mean = models.BooleanField()
    depth_mean_min = models.FloatField(null=True, blank=True)
    depth_mean_max = models.FloatField(null=True, blank=True)

    divefish_overlap = models.BooleanField()
    divefish_overlap_min = models.FloatField(null=True, blank=True)
    divefish_overlap_max = models.FloatField(null=True, blank=True)

    extdive_use = models.BooleanField()
    extdive_use_min = models.FloatField(null=True, blank=True)
    extdive_use_max = models.FloatField(null=True, blank=True)

    impacted = models.BooleanField()
    impacted_input = models.TextField(null=True, blank=True)

    injury_site = models.BooleanField()
    injury_site_input = models.TextField(null=True, blank=True)

    inlet_distance = models.BooleanField()
    inlet_distance_min = models.FloatField(null=True, blank=True)
    inlet_distance_max = models.FloatField(null=True, blank=True)

    large_live_coral = models.BooleanField()
    large_live_coral_input = models.TextField(null=True, blank=True)

    mooring_buoy = models.BooleanField()
    mooring_buoy_input = models.TextField(null=True, blank=True)

    mooring_desc = models.BooleanField()
    mooring_desc_input = models.TextField(null=True, blank=True)

    outfall_distance = models.BooleanField()
    outfall_distance_min = models.FloatField(null=True, blank=True)
    outfall_distance_max = models.FloatField(null=True, blank=True)

    pier_distance = models.BooleanField()
    pier_distance_min = models.FloatField(null=True, blank=True)
    pier_distance_max = models.FloatField(null=True, blank=True)

    pillar_presence = models.BooleanField()
    pillar_presence_input = models.TextField(null=True, blank=True)

    prcnt_art = models.BooleanField()
    prcnt_art_min = models.FloatField(null=True, blank=True)
    prcnt_art_max = models.FloatField(null=True, blank=True)

    prcnt_reef = models.BooleanField()
    prcnt_reef_min = models.FloatField(null=True, blank=True)
    prcnt_reef_max = models.FloatField(null=True, blank=True)

    prcnt_sand = models.BooleanField()
    prcnt_sand_min = models.FloatField(null=True, blank=True)
    prcnt_sand_max = models.FloatField(null=True, blank=True)

    prcnt_sg = models.BooleanField()
    prcnt_sg_min = models.FloatField(null=True, blank=True)
    prcnt_sg_max = models.FloatField(null=True, blank=True)

    reccom_fish = models.BooleanField()
    reccom_fish_min = models.FloatField(null=True, blank=True)
    reccom_fish_max = models.FloatField(null=True, blank=True)

    recfish_use = models.BooleanField()
    recfish_use_min = models.FloatField(null=True, blank=True)
    recfish_use_max = models.FloatField(null=True, blank=True)

    reef_fish_density = models.BooleanField()
    reef_fish_density_min = models.FloatField(null=True, blank=True)
    reef_fish_density_max = models.FloatField(null=True, blank=True)

    reef_fish_richness = models.BooleanField()
    reef_fish_richness_min = models.FloatField(null=True, blank=True)
    reef_fish_richness_max = models.FloatField(null=True, blank=True)

    scuba_use = models.BooleanField()
    scuba_use_min = models.FloatField(null=True, blank=True)
    scuba_use_max = models.FloatField(null=True, blank=True)

    shore_distance = models.BooleanField()
    shore_distance_min = models.FloatField(null=True, blank=True)
    shore_distance_max = models.FloatField(null=True, blank=True)

    spear_use = models.BooleanField()
    spear_use_min = models.FloatField(null=True, blank=True)
    spear_use_max = models.FloatField(null=True, blank=True)

    sponge = models.BooleanField()
    sponge_min = models.FloatField(null=True, blank=True)
    sponge_max = models.FloatField(null=True, blank=True)

    total_use = models.BooleanField()
    total_use_min = models.FloatField(null=True, blank=True)
    total_use_max = models.FloatField(null=True, blank=True)

    watersport_use = models.BooleanField()
    watersport_use_min = models.FloatField(null=True, blank=True)
    watersport_use_max = models.FloatField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    satisfied = models.BooleanField(default=True, help_text="Am I satisfied?")
    active = models.BooleanField(default=True)

    grid_cells = models.TextField(verbose_name='Grid Cell IDs', null=True, blank=True)
    geometry_final_area = models.FloatField(verbose_name='Total Area', null=True, blank=True)
    geometry_dissolved = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Filter result dissolved")

    @property
    def serialize_attributes(self):
        """
        Return attributes in text format. Used to display information on click in the planner.
        """
        attributes = []

        if self.acropora_pa:
            if self.acropora_pa_input == 'Y':
                title = 'Intersects with at least one known dense Acropora patch'
            else:
                title = 'Does not intersect with any known dense Acropora patches'
            attributes.append({'title': title, 'data':  ''})

        if self.anchor_desc:
            attributes.append({'title': 'Anchorage',
                               'data': self.anchor_desc_input})

        if self.anchorage:
            if self.acropora_pa_input == 'Y':
                title = 'Intersects with a designated anchorage'
            else:
                title = 'Does not intersect with any designated anchorages'
            attributes.append({'title': title, 'data':  ''})

        if self.boat_use:
            d = "%s to %s" % (self.boat_use_min, self.boat_use_max)
            attributes.append({'title': 'Boater Use Intensity (OFR 2015)', 'data': d})

        if self.coral_bleach:
            d = "%s to %s" % (self.coral_bleach_min, self.coral_bleach_max)
            attributes.append({'title': 'Coral Bleaching', 'data': d})

        if self.coral_cover:
            d = "%s to %s" % (self.coral_cover_min, self.coral_cover_max)
            attributes.append({'title': 'Coral Percent Cover', 'data': d})

        if self.coral_density:
            attributes.append({'title': 'Minimum estimated coral organisms per sq meter',
                               'data':  str(int(self.coral_density_max))})

        if self.coral_disease:
            d = "%s to %s" % (self.coral_disease_min, self.coral_disease_max)
            attributes.append({'title': 'Coral Disease', 'data': d})

        if self.coral_resilience:
            d = "%s to %s" % (self.coral_resilience_min, self.coral_resilience_max)
            attributes.append({'title': 'Coral resilience', 'data': d})

        if self.coral_richness:
            attributes.append({'title': 'Minimum estimated coral species per survey area',
                               'data':  str(int(self.coral_richness_max))})

        if self.coral_soft:
            d = "%s to %s" % (self.coral_soft_min, self.coral_soft_max)
            attributes.append({'title': 'Soft Coral Percent Cover', 'data': d})

        if self.depth_mean:
            attributes.append({'title': 'Depth Range',
                               'data':  str(int(self.depth_mean_min)) + ' to ' + str(int(self.depth_mean_max)) + ' meters'})

        if self.divefish_overlap:
            d = "%s to %s" % (self.divefish_overlap_min, self.divefish_overlap_max)
            attributes.append({'title': 'Diving and Fishing use overlap (OFR 2015)', 'data': d})

        if self.extdive_use:
            d = "%s to %s" % (self.extdive_use_min, self.extdive_use_max)
            attributes.append({'title': 'Extractive Diving Use Intensity (OFR 2015)', 'data': d})

        if self.impacted:
            if self.acropora_pa_input == 'Y':
                title = 'Intersects with a mapped impact source (artificial reefs, dredged areas, cables, reef injuries, anchorages, burials, etc.)'
            else:
                title = 'Does not intersect with any mapped impact sources (artificial reefs, dredged areas, cables, reef injuries, anchorages, burials, etc.)'
            attributes.append({'title': title, 'data':  ''})

        if self.injury_site:
            if self.injury_site_input == 'Y':
                title = 'Contains at least one recorded grounding or anchoring event in the DEP database'
            else:
                title = 'Does not contain any recorded grounding or anchoring events'
            attributes.append({'title': title, 'data':  ''})

        if self.inlet_distance:
            attributes.append({'title': 'Minimum Distance to Coastal Inlet',
                               'data':  str(self.inlet_distance_min) + ' km'})

        if self.large_live_coral:
            if self.large_live_coral_input == 'Y':
                title = 'Contains at least one known live coral greater than 2 meters in width'
            else:
                title = 'Does not contain any known live coral greater than 2 meters in width'
            attributes.append({'title': title, 'data':  ''})

        if self.mooring_buoy:
            if self.acropora_pa_input == 'Y':
                title = 'Contains at least one Mooring buoy'
            else:
                title = 'Does not contain any Mooring buoys'
            attributes.append({'title': title, 'data':  ''})

        if self.mooring_desc:
            attributes.append({'title': 'Mooring',
                               'data': self.mooring_desc_input})

        if self.outfall_distance:
            attributes.append({'title': 'Minimum Distance to Outfall',
                               'data':  str(self.outfall_distance_min) + ' km'})

        if self.pier_distance:
            attributes.append({'title': 'Distance to Pier',
                               'data':  str(self.pier_distance_min) + ' to ' + str(self.pier_distance_max) + ' km'})

        if self.pillar_presence:
            if self.acropora_pa_input == 'P':
                title = 'Contains at least one recorded Pillar Coral'
            else:
                title = 'Does not contain any recorded Pillar Corals'
            attributes.append({'title': title, 'data':  ''})

        if self.prcnt_art:
            attributes.append({'title': 'Minimum amount of Artificial Substrate',
                               'data':  str(int(self.prcnt_art_min)) + '%'})
        if self.prcnt_reef:
            attributes.append({'title': 'Minimum amount of Reef',
                               'data':  str(int(self.prcnt_reef_min)) + '%'})
        if self.prcnt_sand:
            attributes.append({'title': 'Minimum amount of Sand',
                               'data':  str(int(self.prcnt_sand_min)) + '%'})
        if self.prcnt_sg:
            attributes.append({'title': 'Minimum amount of Seagrass',
                               'data':  str(int(self.prcnt_sg_min)) + '%'})

        if self.reccom_fish:
            d = "%s to %s" % (self.reccom_fish_min, self.reccom_fish_max)
            attributes.append({'title': 'Recreationally and commercially important fishes', 'data': d})

        if self.recfish_use:
            d = "%s to %s" % (self.recfish_use_min, self.recfish_use_max)
            attributes.append({'title': 'Recreational Fishing Use Intensity (OFR 2015)', 'data': d})

        if self.reef_fish_density:
            d = "%s to %s" % (self.reef_fish_density_min, self.reef_fish_density_max)
            attributes.append({'title': 'Relative Reef Fish Density', 'data': d})

        if self.reef_fish_richness:
            d = "%s to %s" % (self.reef_fish_richness_min, self.reef_fish_richness_max)
            attributes.append({'title': 'Number of Reef Fish Species', 'data': d})

        if self.scuba_use:
            d = "%s to %s" % (self.scuba_use_min, self.scuba_use_max)
            attributes.append({'title': 'Scuba Diving Use Intensity (OFR 2015)', 'data': d})

        if self.shore_distance:
            attributes.append({'title': 'Distance to Shore',
                               'data':  str(self.shore_distance_min) + ' to ' + str(self.shore_distance_max) + ' km'})

        if self.spear_use:
            d = "%s to %s" % (self.spear_use_min, self.spear_use_max)
            attributes.append({'title': 'Spearfishing Use Intensity (OFR 2015)', 'data': d})

        if self.sponge:
            d = "%s to %s" % (self.sponge_min, self.sponge_max)
            attributes.append({'title': 'Sponge Percent Cover', 'data': d})

        if self.total_use:
            d = "%s to %s" % (self.total_use_min, self.total_use_max)
            attributes.append({'title': 'Total Use Intensity (OFR 2015)', 'data': d})

        if self.watersport_use:
            d = "%s to %s" % (self.watersport_use_min, self.watersport_use_max)
            attributes.append({'title': 'Water Sports (OFR 2015)', 'data': d})

        attributes.append({'title': 'Number of Grid Cells',
                           'data': '{:,}'.format(self.grid_cells.count(',')+1)})
        return { 'event': 'click', 'attributes': attributes }

    def geojson(self, srid):
        props = get_properties_json(self)
        props['absolute_url'] = self.get_absolute_url()
        json_geom = self.geometry_dissolved.transform(srid, clone=True).json
        return get_feature_json(json_geom, json.dumps(props))

    def run(self):
        # placing this import here to avoid circular dependency with views.py
        from views import run_filter_query
        query = run_filter_query(model_to_dict(self))

        if len(query) == 0:
            self.satisfied = False;
            # raise Exception("No lease blocks available with the current filters.")

        dissolved_geom = query.aggregate(Union('geometry'))
        if dissolved_geom['geometry__union']:
            dissolved_geom = dissolved_geom['geometry__union']
        else:
            raise Exception("No lease blocks available with the current filters.")

        if type(dissolved_geom) == MultiPolygon:
            self.geometry_dissolved = dissolved_geom
        else:
            self.geometry_dissolved = MultiPolygon(dissolved_geom, srid=dissolved_geom.srid)

        self.active = True # ??

        self.geometry_final_area = self.geometry_dissolved.area

        self.grid_cells = ','.join(str(i)
                                     for i in query.values_list('id', flat=True))

        if self.grid_cells == '':
            self.satisfied = False
        else:
            self.satisfied = True
        return True

    def save(self, rerun=None, *args, **kwargs):
        if rerun is None and self.pk is None:
            rerun = True
        if rerun is None and self.pk is not None: #if editing a scenario and no value for rerun is given
            rerun = False
            if not rerun:
                orig = Scenario.objects.get(pk=self.pk)
                #TODO: keeping this in here til I figure out why self.grid_cells and self.geometry_final_area are emptied when run() is not called
                rerun = True
                if not rerun:
                    for f in Scenario.input_fields():
                        # Is original value different from form value?
                        if getattr(orig, f.name) != getattr(self, f.name):
                            #print 'input_field, %s, has changed' %f.name
                            rerun = True
                            break
                if not rerun:
                    '''
                        the substrates need to be grabbed, then saved, then grabbed again because
                        both getattr calls (orig and self) return the same original list until the model has been saved
                        (perhaps because form.save_m2m has to be called), after which calls to getattr will
                        return the same list (regardless of whether we use orig or self)
                    '''
                    orig_weas = set(getattr(self, 'input_wea').all())
                    orig_substrates = set(getattr(self, 'input_substrate').all())
                    orig_sediments = set(getattr(self, 'input_sediment').all())
                    super(Scenario, self).save(rerun=False, *args, **kwargs)
                    new_weas = set(getattr(self, 'input_wea').all())
                    new_substrates = set(getattr(self, 'input_substrate').all())
                    new_sediments = set(getattr(self, 'input_sediment').all())
                    if orig_substrates != new_substrates or orig_sediments != new_sediments or orig_weas != new_weas:
                        rerun = True
            super(Scenario, self).save(rerun=rerun, *args, **kwargs)
        else: #editing a scenario and rerun is provided
            super(Scenario, self).save(rerun=rerun, *args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name

    def support_filename(self):
        return os.path.basename(self.support_file.name)

    @classmethod
    def mapnik_geomfield(self):
        return "output_geom"

    @classmethod
    def mapnik_style(self):
        import mapnik
        polygon_style = mapnik.Style()

        ps = mapnik.PolygonSymbolizer(mapnik.Color('#ffffff'))
        ps.fill_opacity = 0.5

        ls = mapnik.LineSymbolizer(mapnik.Color('#555555'),0.75)
        ls.stroke_opacity = 0.5

        r = mapnik.Rule()
        r.symbols.append(ps)
        r.symbols.append(ls)
        polygon_style.rules.append(r)
        return polygon_style

    @classmethod
    def input_parameter_fields(klass):
        return [f for f in klass._meta.fields if f.attname.startswith('input_parameter_')]

    @classmethod
    def input_filter_fields(klass):
        return [f for f in klass._meta.fields if f.attname.startswith('input_filter_')]

    @property
    def grid_cells_set(self):
        if len(self.grid_cells) == 0:  #empty result
            gridcell_ids = []
        else:
            gridcell_ids = [int(id) for id in self.grid_cells.split(',')]
        gridcells = GridCell.objects.filter(pk__in=gridcell_ids)
        return gridcells

    @property
    def num_lease_blocks(self):
        if self.grid_cells == '':
            return 0
        return len(self.grid_cells.split(','))

    @property
    def geometry_is_empty(self):
        return len(self.grid_cells) == 0

    @property
    def input_wea_names(self):
        return [wea.wea_name for wea in self.input_wea.all()]

    @property
    def input_substrate_names(self):
        return [substrate.substrate_name for substrate in self.input_substrate.all()]

    @property
    def input_sediment_names(self):
        return [sediment.sediment_name for sediment in self.input_sediment.all()]

    #TODO: is this being used...?  Yes, see show.html
    @property
    def has_wind_energy_criteria(self):
        wind_parameters = Scenario.input_parameter_fields()
        for wp in wind_parameters:
            if getattr(self, wp.name):
                return True
        return False

    @property
    def has_shipping_filters(self):
        shipping_filters = Scenario.input_filter_fields()
        for sf in shipping_filters:
            if getattr(self, sf.name):
                return True
        return False

    @property
    def has_military_filters(self):
        return False

    @property
    def color(self):
        try:
            return Objective.objects.get(pk=self.input_objectives.values_list()[0][0]).color
        except:
            return '778B1A55'

    @property
    def get_id(self):
        return self.id

    class Options:
        verbose_name = 'Spatial Design for Wind Energy'
        icon_url = 'marco/img/multi.png'
        form = 'scenarios.forms.ScenarioForm'
        form_template = 'scenario/form.html'
        show_template = 'scenario/show.html'

#no longer needed?
# class Objective(models.Model):
#     name = models.CharField(max_length=35)
#     color = models.CharField(max_length=8, default='778B1A55')

#     def __unicode__(self):
#         return u'%s' % self.name

#no longer needed?
# class Parameter(models.Model):
#     ordering_id = models.IntegerField(null=True, blank=True)
#     name = models.CharField(max_length=35, null=True, blank=True)
#     shortname = models.CharField(max_length=35, null=True, blank=True)
#     objectives = models.ManyToManyField("Objective", null=True, blank=True)

#     def __unicode__(self):
#         return u'%s' % self.name

class GridCell(models.Model):

    acerv_area = models.IntegerField(null=True, blank=True)
    acropora_pa = models.TextField(null=True, blank=True)
    anchor_density = models.FloatField(null=True, blank=True)
    anchor_desc = models.TextField(null=True, blank=True)
    anchorage = models.TextField(null=True, blank=True)
    art_area = models.IntegerField(null=True, blank=True)
    boat_use = models.IntegerField(null=True, blank=True)
    comfish_use = models.IntegerField(null=True, blank=True)
    coral_bleach = models.FloatField(null=True, blank=True)
    coral_cover = models.FloatField(null=True, blank=True)
    coral_density = models.FloatField(null=True, blank=True)
    coral_disease = models.FloatField(null=True, blank=True)
    coral_resilience = models.IntegerField(null=True, blank=True)
    coral_richness = models.FloatField(null=True, blank=True)
    coral_soft = models.FloatField(null=True, blank=True)
    county = models.TextField(null=True, blank=True)
    depth_max = models.FloatField(null=True, blank=True)
    depth_mean = models.FloatField(null=True, blank=True)
    depth_min = models.FloatField(null=True, blank=True)
    divefish_overlap = models.IntegerField(null=True, blank=True)
    extdive_use = models.IntegerField(null=True, blank=True)
    impacted = models.TextField(null=True, blank=True)
    injury_site = models.TextField(null=True, blank=True)
    inlet_distance = models.FloatField(null=True, blank=True)
    large_live_coral = models.TextField(null=True, blank=True)
    mooring_buoy = models.TextField(null=True, blank=True)
    mooring_density = models.FloatField(null=True, blank=True)
    mooring_desc = models.TextField(null=True, blank=True)
    outfall_distance = models.FloatField(null=True, blank=True)
    pier_distance = models.FloatField(null=True, blank=True)
    pillar_presence = models.TextField(null=True, blank=True)
    prcnt_art = models.IntegerField(null=True, blank=True)
    prcnt_reef = models.IntegerField(null=True, blank=True)
    prcnt_sand = models.IntegerField(null=True, blank=True)
    prcnt_sg = models.IntegerField(null=True, blank=True)
    reccom_fish = models.FloatField(null=True, blank=True)
    recfish_use = models.IntegerField(null=True, blank=True)
    reef_area = models.IntegerField(null=True, blank=True)
    reef_fish_density = models.FloatField(null=True, blank=True)
    reef_fish_richness = models.FloatField(null=True, blank=True)
    region = models.TextField(null=True, blank=True)
    research_use = models.IntegerField(null=True, blank=True)
    sand_area = models.IntegerField(null=True, blank=True)
    scuba_use = models.IntegerField(null=True, blank=True)
    sg_area = models.IntegerField(null=True, blank=True)
    shore_distance = models.FloatField(null=True, blank=True)
    spear_use = models.IntegerField(null=True, blank=True)
    sponge = models.FloatField(null=True, blank=True)
    total_use = models.IntegerField(null=True, blank=True)
    unique_id = models.IntegerField(null=True, blank=True)
    watersport_use = models.IntegerField(null=True, blank=True)

    centroid = models.PointField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID,
                                    null=True, blank=True,
                                    verbose_name="Grid Cell Geometry")
    objects = models.GeoManager()

