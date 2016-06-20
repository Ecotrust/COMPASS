# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Scenario.prcnt_sand_max'
        db.delete_column(u'scenarios_scenario', 'prcnt_sand_max')

        # Deleting field 'Scenario.injury_site_input'
        db.delete_column(u'scenarios_scenario', 'injury_site_input')

        # Deleting field 'Scenario.boat_use'
        db.delete_column(u'scenarios_scenario', 'boat_use')

        # Deleting field 'Scenario.coral_bleach'
        db.delete_column(u'scenarios_scenario', 'coral_bleach')

        # Deleting field 'Scenario.anchor_desc'
        db.delete_column(u'scenarios_scenario', 'anchor_desc')

        # Deleting field 'Scenario.spear_use_min'
        db.delete_column(u'scenarios_scenario', 'spear_use_min')

        # Deleting field 'Scenario.spear_use'
        db.delete_column(u'scenarios_scenario', 'spear_use')

        # Deleting field 'Scenario.divefish_overlap_min'
        db.delete_column(u'scenarios_scenario', 'divefish_overlap_min')

        # Deleting field 'Scenario.reccom_fish'
        db.delete_column(u'scenarios_scenario', 'reccom_fish')

        # Deleting field 'Scenario.shore_distance_max'
        db.delete_column(u'scenarios_scenario', 'shore_distance_max')

        # Deleting field 'Scenario.divefish_overlap_max'
        db.delete_column(u'scenarios_scenario', 'divefish_overlap_max')

        # Deleting field 'Scenario.coral_richness_min'
        db.delete_column(u'scenarios_scenario', 'coral_richness_min')

        # Deleting field 'Scenario.shore_distance'
        db.delete_column(u'scenarios_scenario', 'shore_distance')

        # Deleting field 'Scenario.shore_distance_min'
        db.delete_column(u'scenarios_scenario', 'shore_distance_min')

        # Deleting field 'Scenario.coral_richness_max'
        db.delete_column(u'scenarios_scenario', 'coral_richness_max')

        # Deleting field 'Scenario.pier_distance'
        db.delete_column(u'scenarios_scenario', 'pier_distance')

        # Deleting field 'Scenario.depth_mean_min'
        db.delete_column(u'scenarios_scenario', 'depth_mean_min')

        # Deleting field 'Scenario.outfall_distance'
        db.delete_column(u'scenarios_scenario', 'outfall_distance')

        # Deleting field 'Scenario.depth_mean_max'
        db.delete_column(u'scenarios_scenario', 'depth_mean_max')

        # Deleting field 'Scenario.total_use_max'
        db.delete_column(u'scenarios_scenario', 'total_use_max')

        # Deleting field 'Scenario.coral_soft'
        db.delete_column(u'scenarios_scenario', 'coral_soft')

        # Deleting field 'Scenario.coral_bleach_min'
        db.delete_column(u'scenarios_scenario', 'coral_bleach_min')

        # Deleting field 'Scenario.prcnt_reef'
        db.delete_column(u'scenarios_scenario', 'prcnt_reef')

        # Deleting field 'Scenario.inlet_distance_max'
        db.delete_column(u'scenarios_scenario', 'inlet_distance_max')

        # Deleting field 'Scenario.reef_fish_density'
        db.delete_column(u'scenarios_scenario', 'reef_fish_density')

        # Deleting field 'Scenario.pillar_presence_input'
        db.delete_column(u'scenarios_scenario', 'pillar_presence_input')

        # Deleting field 'Scenario.sponge'
        db.delete_column(u'scenarios_scenario', 'sponge')

        # Deleting field 'Scenario.acropora_pa'
        db.delete_column(u'scenarios_scenario', 'acropora_pa')

        # Deleting field 'Scenario.prcnt_sg'
        db.delete_column(u'scenarios_scenario', 'prcnt_sg')

        # Deleting field 'Scenario.large_live_coral_input'
        db.delete_column(u'scenarios_scenario', 'large_live_coral_input')

        # Deleting field 'Scenario.sponge_max'
        db.delete_column(u'scenarios_scenario', 'sponge_max')

        # Deleting field 'Scenario.extdive_use_min'
        db.delete_column(u'scenarios_scenario', 'extdive_use_min')

        # Deleting field 'Scenario.extdive_use_max'
        db.delete_column(u'scenarios_scenario', 'extdive_use_max')

        # Deleting field 'Scenario.sponge_min'
        db.delete_column(u'scenarios_scenario', 'sponge_min')

        # Deleting field 'Scenario.scuba_use_min'
        db.delete_column(u'scenarios_scenario', 'scuba_use_min')

        # Deleting field 'Scenario.reef_fish_density_min'
        db.delete_column(u'scenarios_scenario', 'reef_fish_density_min')

        # Deleting field 'Scenario.acropora_pa_input'
        db.delete_column(u'scenarios_scenario', 'acropora_pa_input')

        # Deleting field 'Scenario.reef_fish_density_max'
        db.delete_column(u'scenarios_scenario', 'reef_fish_density_max')

        # Deleting field 'Scenario.mooring_desc'
        db.delete_column(u'scenarios_scenario', 'mooring_desc')

        # Deleting field 'Scenario.impacted_input'
        db.delete_column(u'scenarios_scenario', 'impacted_input')

        # Deleting field 'Scenario.recfish_use'
        db.delete_column(u'scenarios_scenario', 'recfish_use')

        # Deleting field 'Scenario.anchorage'
        db.delete_column(u'scenarios_scenario', 'anchorage')

        # Deleting field 'Scenario.prcnt_sand'
        db.delete_column(u'scenarios_scenario', 'prcnt_sand')

        # Deleting field 'Scenario.prcnt_sand_min'
        db.delete_column(u'scenarios_scenario', 'prcnt_sand_min')

        # Deleting field 'Scenario.coral_bleach_max'
        db.delete_column(u'scenarios_scenario', 'coral_bleach_max')

        # Deleting field 'Scenario.watersport_use_max'
        db.delete_column(u'scenarios_scenario', 'watersport_use_max')

        # Deleting field 'Scenario.watersport_use_min'
        db.delete_column(u'scenarios_scenario', 'watersport_use_min')

        # Deleting field 'Scenario.spear_use_max'
        db.delete_column(u'scenarios_scenario', 'spear_use_max')

        # Deleting field 'Scenario.prcnt_art'
        db.delete_column(u'scenarios_scenario', 'prcnt_art')

        # Deleting field 'Scenario.pier_distance_min'
        db.delete_column(u'scenarios_scenario', 'pier_distance_min')

        # Deleting field 'Scenario.depth_mean'
        db.delete_column(u'scenarios_scenario', 'depth_mean')

        # Deleting field 'Scenario.inlet_distance'
        db.delete_column(u'scenarios_scenario', 'inlet_distance')

        # Deleting field 'Scenario.reef_fish_richness'
        db.delete_column(u'scenarios_scenario', 'reef_fish_richness')

        # Deleting field 'Scenario.mooring_desc_input'
        db.delete_column(u'scenarios_scenario', 'mooring_desc_input')

        # Deleting field 'Scenario.outfall_distance_max'
        db.delete_column(u'scenarios_scenario', 'outfall_distance_max')

        # Deleting field 'Scenario.coral_soft_min'
        db.delete_column(u'scenarios_scenario', 'coral_soft_min')

        # Deleting field 'Scenario.injury_site'
        db.delete_column(u'scenarios_scenario', 'injury_site')

        # Deleting field 'Scenario.coral_soft_max'
        db.delete_column(u'scenarios_scenario', 'coral_soft_max')

        # Deleting field 'Scenario.large_live_coral'
        db.delete_column(u'scenarios_scenario', 'large_live_coral')

        # Deleting field 'Scenario.pillar_presence'
        db.delete_column(u'scenarios_scenario', 'pillar_presence')

        # Deleting field 'Scenario.outfall_distance_min'
        db.delete_column(u'scenarios_scenario', 'outfall_distance_min')

        # Deleting field 'Scenario.divefish_overlap'
        db.delete_column(u'scenarios_scenario', 'divefish_overlap')

        # Deleting field 'Scenario.anchor_desc_input'
        db.delete_column(u'scenarios_scenario', 'anchor_desc_input')

        # Deleting field 'Scenario.coral_density_max'
        db.delete_column(u'scenarios_scenario', 'coral_density_max')

        # Deleting field 'Scenario.coral_density_min'
        db.delete_column(u'scenarios_scenario', 'coral_density_min')

        # Deleting field 'Scenario.extdive_use'
        db.delete_column(u'scenarios_scenario', 'extdive_use')

        # Deleting field 'Scenario.total_use'
        db.delete_column(u'scenarios_scenario', 'total_use')

        # Deleting field 'Scenario.mooring_buoy'
        db.delete_column(u'scenarios_scenario', 'mooring_buoy')

        # Deleting field 'Scenario.impacted'
        db.delete_column(u'scenarios_scenario', 'impacted')

        # Deleting field 'Scenario.coral_disease_max'
        db.delete_column(u'scenarios_scenario', 'coral_disease_max')

        # Deleting field 'Scenario.prcnt_reef_max'
        db.delete_column(u'scenarios_scenario', 'prcnt_reef_max')

        # Deleting field 'Scenario.total_use_min'
        db.delete_column(u'scenarios_scenario', 'total_use_min')

        # Deleting field 'Scenario.recfish_use_min'
        db.delete_column(u'scenarios_scenario', 'recfish_use_min')

        # Deleting field 'Scenario.boat_use_min'
        db.delete_column(u'scenarios_scenario', 'boat_use_min')

        # Deleting field 'Scenario.boat_use_max'
        db.delete_column(u'scenarios_scenario', 'boat_use_max')

        # Deleting field 'Scenario.scuba_use_max'
        db.delete_column(u'scenarios_scenario', 'scuba_use_max')

        # Deleting field 'Scenario.coral_disease'
        db.delete_column(u'scenarios_scenario', 'coral_disease')

        # Deleting field 'Scenario.watersport_use'
        db.delete_column(u'scenarios_scenario', 'watersport_use')

        # Deleting field 'Scenario.inlet_distance_min'
        db.delete_column(u'scenarios_scenario', 'inlet_distance_min')

        # Deleting field 'Scenario.reccom_fish_max'
        db.delete_column(u'scenarios_scenario', 'reccom_fish_max')

        # Deleting field 'Scenario.coral_cover'
        db.delete_column(u'scenarios_scenario', 'coral_cover')

        # Deleting field 'Scenario.reccom_fish_min'
        db.delete_column(u'scenarios_scenario', 'reccom_fish_min')

        # Deleting field 'Scenario.coral_resilience_max'
        db.delete_column(u'scenarios_scenario', 'coral_resilience_max')

        # Deleting field 'Scenario.recfish_use_max'
        db.delete_column(u'scenarios_scenario', 'recfish_use_max')

        # Deleting field 'Scenario.coral_richness'
        db.delete_column(u'scenarios_scenario', 'coral_richness')

        # Deleting field 'Scenario.coral_resilience_min'
        db.delete_column(u'scenarios_scenario', 'coral_resilience_min')

        # Deleting field 'Scenario.prcnt_reef_min'
        db.delete_column(u'scenarios_scenario', 'prcnt_reef_min')

        # Deleting field 'Scenario.coral_disease_min'
        db.delete_column(u'scenarios_scenario', 'coral_disease_min')

        # Deleting field 'Scenario.coral_density'
        db.delete_column(u'scenarios_scenario', 'coral_density')

        # Deleting field 'Scenario.anchorage_input'
        db.delete_column(u'scenarios_scenario', 'anchorage_input')

        # Deleting field 'Scenario.coral_cover_min'
        db.delete_column(u'scenarios_scenario', 'coral_cover_min')

        # Deleting field 'Scenario.pier_distance_max'
        db.delete_column(u'scenarios_scenario', 'pier_distance_max')

        # Deleting field 'Scenario.scuba_use'
        db.delete_column(u'scenarios_scenario', 'scuba_use')

        # Deleting field 'Scenario.reef_fish_richness_min'
        db.delete_column(u'scenarios_scenario', 'reef_fish_richness_min')

        # Deleting field 'Scenario.coral_resilience'
        db.delete_column(u'scenarios_scenario', 'coral_resilience')

        # Deleting field 'Scenario.reef_fish_richness_max'
        db.delete_column(u'scenarios_scenario', 'reef_fish_richness_max')

        # Deleting field 'Scenario.coral_cover_max'
        db.delete_column(u'scenarios_scenario', 'coral_cover_max')

        # Deleting field 'Scenario.prcnt_art_max'
        db.delete_column(u'scenarios_scenario', 'prcnt_art_max')

        # Deleting field 'Scenario.prcnt_sg_max'
        db.delete_column(u'scenarios_scenario', 'prcnt_sg_max')

        # Deleting field 'Scenario.prcnt_sg_min'
        db.delete_column(u'scenarios_scenario', 'prcnt_sg_min')

        # Deleting field 'Scenario.mooring_buoy_input'
        db.delete_column(u'scenarios_scenario', 'mooring_buoy_input')

        # Deleting field 'Scenario.prcnt_art_min'
        db.delete_column(u'scenarios_scenario', 'prcnt_art_min')

        # Adding field 'Scenario.habitat'
        db.add_column(u'scenarios_scenario', 'habitat',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.fish'
        db.add_column(u'scenarios_scenario', 'fish',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.obs_spec'
        db.add_column(u'scenarios_scenario', 'obs_spec',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.mod_spec'
        db.add_column(u'scenarios_scenario', 'mod_spec',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'GridCell.prcnt_art'
        db.delete_column(u'scenarios_gridcell', 'prcnt_art')

        # Deleting field 'GridCell.reccom_fish'
        db.delete_column(u'scenarios_gridcell', 'reccom_fish')

        # Deleting field 'GridCell.depth_mean'
        db.delete_column(u'scenarios_gridcell', 'depth_mean')

        # Deleting field 'GridCell.boat_use'
        db.delete_column(u'scenarios_gridcell', 'boat_use')

        # Deleting field 'GridCell.coral_bleach'
        db.delete_column(u'scenarios_gridcell', 'coral_bleach')

        # Deleting field 'GridCell.county'
        db.delete_column(u'scenarios_gridcell', 'county')

        # Deleting field 'GridCell.anchor_desc'
        db.delete_column(u'scenarios_gridcell', 'anchor_desc')

        # Deleting field 'GridCell.reef_area'
        db.delete_column(u'scenarios_gridcell', 'reef_area')

        # Deleting field 'GridCell.sg_area'
        db.delete_column(u'scenarios_gridcell', 'sg_area')

        # Deleting field 'GridCell.mooring_density'
        db.delete_column(u'scenarios_gridcell', 'mooring_density')

        # Deleting field 'GridCell.injury_site'
        db.delete_column(u'scenarios_gridcell', 'injury_site')

        # Deleting field 'GridCell.shore_distance'
        db.delete_column(u'scenarios_gridcell', 'shore_distance')

        # Deleting field 'GridCell.large_live_coral'
        db.delete_column(u'scenarios_gridcell', 'large_live_coral')

        # Deleting field 'GridCell.pillar_presence'
        db.delete_column(u'scenarios_gridcell', 'pillar_presence')

        # Deleting field 'GridCell.divefish_overlap'
        db.delete_column(u'scenarios_gridcell', 'divefish_overlap')

        # Deleting field 'GridCell.coral_resilience'
        db.delete_column(u'scenarios_gridcell', 'coral_resilience')

        # Deleting field 'GridCell.extdive_use'
        db.delete_column(u'scenarios_gridcell', 'extdive_use')

        # Deleting field 'GridCell.total_use'
        db.delete_column(u'scenarios_gridcell', 'total_use')

        # Deleting field 'GridCell.inlet_distance'
        db.delete_column(u'scenarios_gridcell', 'inlet_distance')

        # Deleting field 'GridCell.pier_distance'
        db.delete_column(u'scenarios_gridcell', 'pier_distance')

        # Deleting field 'GridCell.coral_soft'
        db.delete_column(u'scenarios_gridcell', 'coral_soft')

        # Deleting field 'GridCell.prcnt_reef'
        db.delete_column(u'scenarios_gridcell', 'prcnt_reef')

        # Deleting field 'GridCell.sand_area'
        db.delete_column(u'scenarios_gridcell', 'sand_area')

        # Deleting field 'GridCell.mooring_buoy'
        db.delete_column(u'scenarios_gridcell', 'mooring_buoy')

        # Deleting field 'GridCell.comfish_use'
        db.delete_column(u'scenarios_gridcell', 'comfish_use')

        # Deleting field 'GridCell.impacted'
        db.delete_column(u'scenarios_gridcell', 'impacted')

        # Deleting field 'GridCell.region'
        db.delete_column(u'scenarios_gridcell', 'region')

        # Deleting field 'GridCell.reef_fish_density'
        db.delete_column(u'scenarios_gridcell', 'reef_fish_density')

        # Deleting field 'GridCell.depth_min'
        db.delete_column(u'scenarios_gridcell', 'depth_min')

        # Deleting field 'GridCell.depth_max'
        db.delete_column(u'scenarios_gridcell', 'depth_max')

        # Deleting field 'GridCell.coral_disease'
        db.delete_column(u'scenarios_gridcell', 'coral_disease')

        # Deleting field 'GridCell.watersport_use'
        db.delete_column(u'scenarios_gridcell', 'watersport_use')

        # Deleting field 'GridCell.sponge'
        db.delete_column(u'scenarios_gridcell', 'sponge')

        # Deleting field 'GridCell.acropora_pa'
        db.delete_column(u'scenarios_gridcell', 'acropora_pa')

        # Deleting field 'GridCell.prcnt_sg'
        db.delete_column(u'scenarios_gridcell', 'prcnt_sg')

        # Deleting field 'GridCell.coral_cover'
        db.delete_column(u'scenarios_gridcell', 'coral_cover')

        # Deleting field 'GridCell.research_use'
        db.delete_column(u'scenarios_gridcell', 'research_use')

        # Deleting field 'GridCell.reef_fish_richness'
        db.delete_column(u'scenarios_gridcell', 'reef_fish_richness')

        # Deleting field 'GridCell.acerv_area'
        db.delete_column(u'scenarios_gridcell', 'acerv_area')

        # Deleting field 'GridCell.spear_use'
        db.delete_column(u'scenarios_gridcell', 'spear_use')

        # Deleting field 'GridCell.art_area'
        db.delete_column(u'scenarios_gridcell', 'art_area')

        # Deleting field 'GridCell.coral_richness'
        db.delete_column(u'scenarios_gridcell', 'coral_richness')

        # Deleting field 'GridCell.coral_density'
        db.delete_column(u'scenarios_gridcell', 'coral_density')

        # Deleting field 'GridCell.mooring_desc'
        db.delete_column(u'scenarios_gridcell', 'mooring_desc')

        # Deleting field 'GridCell.recfish_use'
        db.delete_column(u'scenarios_gridcell', 'recfish_use')

        # Deleting field 'GridCell.scuba_use'
        db.delete_column(u'scenarios_gridcell', 'scuba_use')

        # Deleting field 'GridCell.anchorage'
        db.delete_column(u'scenarios_gridcell', 'anchorage')

        # Deleting field 'GridCell.prcnt_sand'
        db.delete_column(u'scenarios_gridcell', 'prcnt_sand')

        # Deleting field 'GridCell.anchor_density'
        db.delete_column(u'scenarios_gridcell', 'anchor_density')

        # Deleting field 'GridCell.outfall_distance'
        db.delete_column(u'scenarios_gridcell', 'outfall_distance')

        # Deleting field 'GridCell.unique_id'
        db.delete_column(u'scenarios_gridcell', 'unique_id')

        # Adding field 'GridCell.objectid'
        db.add_column(u'scenarios_gridcell', 'objectid',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.habitat'
        db.add_column(u'scenarios_gridcell', 'habitat',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.fish'
        db.add_column(u'scenarios_gridcell', 'fish',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.obs_spec'
        db.add_column(u'scenarios_gridcell', 'obs_spec',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.mod_spec'
        db.add_column(u'scenarios_gridcell', 'mod_spec',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Scenario.prcnt_sand_max'
        db.add_column(u'scenarios_scenario', 'prcnt_sand_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.injury_site_input'
        db.add_column(u'scenarios_scenario', 'injury_site_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.boat_use'
        db.add_column(u'scenarios_scenario', 'boat_use',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_bleach'
        db.add_column(u'scenarios_scenario', 'coral_bleach',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.anchor_desc'
        db.add_column(u'scenarios_scenario', 'anchor_desc',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.spear_use_min'
        db.add_column(u'scenarios_scenario', 'spear_use_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.spear_use'
        db.add_column(u'scenarios_scenario', 'spear_use',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.divefish_overlap_min'
        db.add_column(u'scenarios_scenario', 'divefish_overlap_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.reccom_fish'
        db.add_column(u'scenarios_scenario', 'reccom_fish',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.shore_distance_max'
        db.add_column(u'scenarios_scenario', 'shore_distance_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.divefish_overlap_max'
        db.add_column(u'scenarios_scenario', 'divefish_overlap_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_richness_min'
        db.add_column(u'scenarios_scenario', 'coral_richness_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.shore_distance'
        db.add_column(u'scenarios_scenario', 'shore_distance',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.shore_distance_min'
        db.add_column(u'scenarios_scenario', 'shore_distance_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_richness_max'
        db.add_column(u'scenarios_scenario', 'coral_richness_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.pier_distance'
        db.add_column(u'scenarios_scenario', 'pier_distance',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.depth_mean_min'
        db.add_column(u'scenarios_scenario', 'depth_mean_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.outfall_distance'
        db.add_column(u'scenarios_scenario', 'outfall_distance',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.depth_mean_max'
        db.add_column(u'scenarios_scenario', 'depth_mean_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.total_use_max'
        db.add_column(u'scenarios_scenario', 'total_use_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_soft'
        db.add_column(u'scenarios_scenario', 'coral_soft',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_bleach_min'
        db.add_column(u'scenarios_scenario', 'coral_bleach_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_reef'
        db.add_column(u'scenarios_scenario', 'prcnt_reef',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.inlet_distance_max'
        db.add_column(u'scenarios_scenario', 'inlet_distance_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.reef_fish_density'
        db.add_column(u'scenarios_scenario', 'reef_fish_density',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.pillar_presence_input'
        db.add_column(u'scenarios_scenario', 'pillar_presence_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.sponge'
        db.add_column(u'scenarios_scenario', 'sponge',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.acropora_pa'
        db.add_column(u'scenarios_scenario', 'acropora_pa',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sg'
        db.add_column(u'scenarios_scenario', 'prcnt_sg',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.large_live_coral_input'
        db.add_column(u'scenarios_scenario', 'large_live_coral_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.sponge_max'
        db.add_column(u'scenarios_scenario', 'sponge_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.extdive_use_min'
        db.add_column(u'scenarios_scenario', 'extdive_use_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.extdive_use_max'
        db.add_column(u'scenarios_scenario', 'extdive_use_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.sponge_min'
        db.add_column(u'scenarios_scenario', 'sponge_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.scuba_use_min'
        db.add_column(u'scenarios_scenario', 'scuba_use_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.reef_fish_density_min'
        db.add_column(u'scenarios_scenario', 'reef_fish_density_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.acropora_pa_input'
        db.add_column(u'scenarios_scenario', 'acropora_pa_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.reef_fish_density_max'
        db.add_column(u'scenarios_scenario', 'reef_fish_density_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.mooring_desc'
        db.add_column(u'scenarios_scenario', 'mooring_desc',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.impacted_input'
        db.add_column(u'scenarios_scenario', 'impacted_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.recfish_use'
        db.add_column(u'scenarios_scenario', 'recfish_use',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.anchorage'
        db.add_column(u'scenarios_scenario', 'anchorage',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sand'
        db.add_column(u'scenarios_scenario', 'prcnt_sand',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sand_min'
        db.add_column(u'scenarios_scenario', 'prcnt_sand_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_bleach_max'
        db.add_column(u'scenarios_scenario', 'coral_bleach_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.watersport_use_max'
        db.add_column(u'scenarios_scenario', 'watersport_use_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.watersport_use_min'
        db.add_column(u'scenarios_scenario', 'watersport_use_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.spear_use_max'
        db.add_column(u'scenarios_scenario', 'spear_use_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_art'
        db.add_column(u'scenarios_scenario', 'prcnt_art',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.pier_distance_min'
        db.add_column(u'scenarios_scenario', 'pier_distance_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.depth_mean'
        db.add_column(u'scenarios_scenario', 'depth_mean',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.inlet_distance'
        db.add_column(u'scenarios_scenario', 'inlet_distance',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.reef_fish_richness'
        db.add_column(u'scenarios_scenario', 'reef_fish_richness',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.mooring_desc_input'
        db.add_column(u'scenarios_scenario', 'mooring_desc_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.outfall_distance_max'
        db.add_column(u'scenarios_scenario', 'outfall_distance_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_soft_min'
        db.add_column(u'scenarios_scenario', 'coral_soft_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.injury_site'
        db.add_column(u'scenarios_scenario', 'injury_site',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_soft_max'
        db.add_column(u'scenarios_scenario', 'coral_soft_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.large_live_coral'
        db.add_column(u'scenarios_scenario', 'large_live_coral',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.pillar_presence'
        db.add_column(u'scenarios_scenario', 'pillar_presence',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.outfall_distance_min'
        db.add_column(u'scenarios_scenario', 'outfall_distance_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.divefish_overlap'
        db.add_column(u'scenarios_scenario', 'divefish_overlap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.anchor_desc_input'
        db.add_column(u'scenarios_scenario', 'anchor_desc_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_density_max'
        db.add_column(u'scenarios_scenario', 'coral_density_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_density_min'
        db.add_column(u'scenarios_scenario', 'coral_density_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.extdive_use'
        db.add_column(u'scenarios_scenario', 'extdive_use',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.total_use'
        db.add_column(u'scenarios_scenario', 'total_use',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.mooring_buoy'
        db.add_column(u'scenarios_scenario', 'mooring_buoy',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.impacted'
        db.add_column(u'scenarios_scenario', 'impacted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_disease_max'
        db.add_column(u'scenarios_scenario', 'coral_disease_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_reef_max'
        db.add_column(u'scenarios_scenario', 'prcnt_reef_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.total_use_min'
        db.add_column(u'scenarios_scenario', 'total_use_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.recfish_use_min'
        db.add_column(u'scenarios_scenario', 'recfish_use_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.boat_use_min'
        db.add_column(u'scenarios_scenario', 'boat_use_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.boat_use_max'
        db.add_column(u'scenarios_scenario', 'boat_use_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.scuba_use_max'
        db.add_column(u'scenarios_scenario', 'scuba_use_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_disease'
        db.add_column(u'scenarios_scenario', 'coral_disease',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.watersport_use'
        db.add_column(u'scenarios_scenario', 'watersport_use',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.inlet_distance_min'
        db.add_column(u'scenarios_scenario', 'inlet_distance_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.reccom_fish_max'
        db.add_column(u'scenarios_scenario', 'reccom_fish_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_cover'
        db.add_column(u'scenarios_scenario', 'coral_cover',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.reccom_fish_min'
        db.add_column(u'scenarios_scenario', 'reccom_fish_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_resilience_max'
        db.add_column(u'scenarios_scenario', 'coral_resilience_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.recfish_use_max'
        db.add_column(u'scenarios_scenario', 'recfish_use_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_richness'
        db.add_column(u'scenarios_scenario', 'coral_richness',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_resilience_min'
        db.add_column(u'scenarios_scenario', 'coral_resilience_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_reef_min'
        db.add_column(u'scenarios_scenario', 'prcnt_reef_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_disease_min'
        db.add_column(u'scenarios_scenario', 'coral_disease_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_density'
        db.add_column(u'scenarios_scenario', 'coral_density',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.anchorage_input'
        db.add_column(u'scenarios_scenario', 'anchorage_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_cover_min'
        db.add_column(u'scenarios_scenario', 'coral_cover_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.pier_distance_max'
        db.add_column(u'scenarios_scenario', 'pier_distance_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.scuba_use'
        db.add_column(u'scenarios_scenario', 'scuba_use',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.reef_fish_richness_min'
        db.add_column(u'scenarios_scenario', 'reef_fish_richness_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_resilience'
        db.add_column(u'scenarios_scenario', 'coral_resilience',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.reef_fish_richness_max'
        db.add_column(u'scenarios_scenario', 'reef_fish_richness_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_cover_max'
        db.add_column(u'scenarios_scenario', 'coral_cover_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_art_max'
        db.add_column(u'scenarios_scenario', 'prcnt_art_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sg_max'
        db.add_column(u'scenarios_scenario', 'prcnt_sg_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sg_min'
        db.add_column(u'scenarios_scenario', 'prcnt_sg_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.mooring_buoy_input'
        db.add_column(u'scenarios_scenario', 'mooring_buoy_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_art_min'
        db.add_column(u'scenarios_scenario', 'prcnt_art_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Scenario.habitat'
        db.delete_column(u'scenarios_scenario', 'habitat')

        # Deleting field 'Scenario.fish'
        db.delete_column(u'scenarios_scenario', 'fish')

        # Deleting field 'Scenario.obs_spec'
        db.delete_column(u'scenarios_scenario', 'obs_spec')

        # Deleting field 'Scenario.mod_spec'
        db.delete_column(u'scenarios_scenario', 'mod_spec')

        # Adding field 'GridCell.prcnt_art'
        db.add_column(u'scenarios_gridcell', 'prcnt_art',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.reccom_fish'
        db.add_column(u'scenarios_gridcell', 'reccom_fish',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.depth_mean'
        db.add_column(u'scenarios_gridcell', 'depth_mean',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.boat_use'
        db.add_column(u'scenarios_gridcell', 'boat_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_bleach'
        db.add_column(u'scenarios_gridcell', 'coral_bleach',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.county'
        db.add_column(u'scenarios_gridcell', 'county',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.anchor_desc'
        db.add_column(u'scenarios_gridcell', 'anchor_desc',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.reef_area'
        db.add_column(u'scenarios_gridcell', 'reef_area',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.sg_area'
        db.add_column(u'scenarios_gridcell', 'sg_area',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.mooring_density'
        db.add_column(u'scenarios_gridcell', 'mooring_density',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.injury_site'
        db.add_column(u'scenarios_gridcell', 'injury_site',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.shore_distance'
        db.add_column(u'scenarios_gridcell', 'shore_distance',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.large_live_coral'
        db.add_column(u'scenarios_gridcell', 'large_live_coral',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.pillar_presence'
        db.add_column(u'scenarios_gridcell', 'pillar_presence',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.divefish_overlap'
        db.add_column(u'scenarios_gridcell', 'divefish_overlap',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_resilience'
        db.add_column(u'scenarios_gridcell', 'coral_resilience',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.extdive_use'
        db.add_column(u'scenarios_gridcell', 'extdive_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.total_use'
        db.add_column(u'scenarios_gridcell', 'total_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.inlet_distance'
        db.add_column(u'scenarios_gridcell', 'inlet_distance',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.pier_distance'
        db.add_column(u'scenarios_gridcell', 'pier_distance',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_soft'
        db.add_column(u'scenarios_gridcell', 'coral_soft',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.prcnt_reef'
        db.add_column(u'scenarios_gridcell', 'prcnt_reef',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.sand_area'
        db.add_column(u'scenarios_gridcell', 'sand_area',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.mooring_buoy'
        db.add_column(u'scenarios_gridcell', 'mooring_buoy',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.comfish_use'
        db.add_column(u'scenarios_gridcell', 'comfish_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.impacted'
        db.add_column(u'scenarios_gridcell', 'impacted',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.region'
        db.add_column(u'scenarios_gridcell', 'region',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.reef_fish_density'
        db.add_column(u'scenarios_gridcell', 'reef_fish_density',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.depth_min'
        db.add_column(u'scenarios_gridcell', 'depth_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.depth_max'
        db.add_column(u'scenarios_gridcell', 'depth_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_disease'
        db.add_column(u'scenarios_gridcell', 'coral_disease',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.watersport_use'
        db.add_column(u'scenarios_gridcell', 'watersport_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.sponge'
        db.add_column(u'scenarios_gridcell', 'sponge',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.acropora_pa'
        db.add_column(u'scenarios_gridcell', 'acropora_pa',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.prcnt_sg'
        db.add_column(u'scenarios_gridcell', 'prcnt_sg',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_cover'
        db.add_column(u'scenarios_gridcell', 'coral_cover',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.research_use'
        db.add_column(u'scenarios_gridcell', 'research_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.reef_fish_richness'
        db.add_column(u'scenarios_gridcell', 'reef_fish_richness',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.acerv_area'
        db.add_column(u'scenarios_gridcell', 'acerv_area',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.spear_use'
        db.add_column(u'scenarios_gridcell', 'spear_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.art_area'
        db.add_column(u'scenarios_gridcell', 'art_area',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_richness'
        db.add_column(u'scenarios_gridcell', 'coral_richness',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_density'
        db.add_column(u'scenarios_gridcell', 'coral_density',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.mooring_desc'
        db.add_column(u'scenarios_gridcell', 'mooring_desc',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.recfish_use'
        db.add_column(u'scenarios_gridcell', 'recfish_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.scuba_use'
        db.add_column(u'scenarios_gridcell', 'scuba_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.anchorage'
        db.add_column(u'scenarios_gridcell', 'anchorage',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.prcnt_sand'
        db.add_column(u'scenarios_gridcell', 'prcnt_sand',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.anchor_density'
        db.add_column(u'scenarios_gridcell', 'anchor_density',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.outfall_distance'
        db.add_column(u'scenarios_gridcell', 'outfall_distance',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.unique_id'
        db.add_column(u'scenarios_gridcell', 'unique_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'GridCell.objectid'
        db.delete_column(u'scenarios_gridcell', 'objectid')

        # Deleting field 'GridCell.habitat'
        db.delete_column(u'scenarios_gridcell', 'habitat')

        # Deleting field 'GridCell.fish'
        db.delete_column(u'scenarios_gridcell', 'fish')

        # Deleting field 'GridCell.obs_spec'
        db.delete_column(u'scenarios_gridcell', 'obs_spec')

        # Deleting field 'GridCell.mod_spec'
        db.delete_column(u'scenarios_gridcell', 'mod_spec')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'scenarios.gridcell': {
            'Meta': {'object_name': 'GridCell'},
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'fish': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'habitat': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mod_spec': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'obs_spec': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'scenarios.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'scenarios_scenario_related'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'geometry_dissolved': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'geometry_final_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'grid_cells': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'habitat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mod_spec': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'obs_spec': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'satisfied': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'scenarios_scenario_related'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'scenarios_scenario_related'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['scenarios']