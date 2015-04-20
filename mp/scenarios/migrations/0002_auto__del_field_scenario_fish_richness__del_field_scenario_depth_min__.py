# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Scenario.fish_richness'
        db.delete_column(u'scenarios_scenario', 'fish_richness')

        # Deleting field 'Scenario.depth_min'
        db.delete_column(u'scenarios_scenario', 'depth_min')

        # Deleting field 'Scenario.depth_max'
        db.delete_column(u'scenarios_scenario', 'depth_max')

        # Deleting field 'Scenario.fish_richness_max'
        db.delete_column(u'scenarios_scenario', 'fish_richness_max')

        # Deleting field 'Scenario.fish_richness_min'
        db.delete_column(u'scenarios_scenario', 'fish_richness_min')

        # Deleting field 'Scenario.depth'
        db.delete_column(u'scenarios_scenario', 'depth')

        # Adding field 'Scenario.anchor_desc'
        db.add_column(u'scenarios_scenario', 'anchor_desc',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.anchor_desc_input'
        db.add_column(u'scenarios_scenario', 'anchor_desc_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.boat_use'
        db.add_column(u'scenarios_scenario', 'boat_use',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.boat_use_min'
        db.add_column(u'scenarios_scenario', 'boat_use_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.boat_use_max'
        db.add_column(u'scenarios_scenario', 'boat_use_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_cover'
        db.add_column(u'scenarios_scenario', 'coral_cover',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_cover_min'
        db.add_column(u'scenarios_scenario', 'coral_cover_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_cover_max'
        db.add_column(u'scenarios_scenario', 'coral_cover_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_soft'
        db.add_column(u'scenarios_scenario', 'coral_soft',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_soft_min'
        db.add_column(u'scenarios_scenario', 'coral_soft_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_soft_max'
        db.add_column(u'scenarios_scenario', 'coral_soft_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.depth_mean'
        db.add_column(u'scenarios_scenario', 'depth_mean',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.depth_mean_min'
        db.add_column(u'scenarios_scenario', 'depth_mean_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.depth_mean_max'
        db.add_column(u'scenarios_scenario', 'depth_mean_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.divefish_overlap'
        db.add_column(u'scenarios_scenario', 'divefish_overlap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.divefish_overlap_min'
        db.add_column(u'scenarios_scenario', 'divefish_overlap_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.divefish_overlap_max'
        db.add_column(u'scenarios_scenario', 'divefish_overlap_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.mooring_desc'
        db.add_column(u'scenarios_scenario', 'mooring_desc',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.mooring_desc_input'
        db.add_column(u'scenarios_scenario', 'mooring_desc_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.reccom_fish'
        db.add_column(u'scenarios_scenario', 'reccom_fish',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.reccom_fish_min'
        db.add_column(u'scenarios_scenario', 'reccom_fish_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.reccom_fish_max'
        db.add_column(u'scenarios_scenario', 'reccom_fish_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.sponge'
        db.add_column(u'scenarios_scenario', 'sponge',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.sponge_min'
        db.add_column(u'scenarios_scenario', 'sponge_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.sponge_max'
        db.add_column(u'scenarios_scenario', 'sponge_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.watersport_use'
        db.add_column(u'scenarios_scenario', 'watersport_use',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.watersport_use_min'
        db.add_column(u'scenarios_scenario', 'watersport_use_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.watersport_use_max'
        db.add_column(u'scenarios_scenario', 'watersport_use_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Scenario.fish_richness'
        db.add_column(u'scenarios_scenario', 'fish_richness',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.depth_min'
        db.add_column(u'scenarios_scenario', 'depth_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.depth_max'
        db.add_column(u'scenarios_scenario', 'depth_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.fish_richness_max'
        db.add_column(u'scenarios_scenario', 'fish_richness_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.fish_richness_min'
        db.add_column(u'scenarios_scenario', 'fish_richness_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.depth'
        db.add_column(u'scenarios_scenario', 'depth',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Scenario.anchor_desc'
        db.delete_column(u'scenarios_scenario', 'anchor_desc')

        # Deleting field 'Scenario.anchor_desc_input'
        db.delete_column(u'scenarios_scenario', 'anchor_desc_input')

        # Deleting field 'Scenario.boat_use'
        db.delete_column(u'scenarios_scenario', 'boat_use')

        # Deleting field 'Scenario.boat_use_min'
        db.delete_column(u'scenarios_scenario', 'boat_use_min')

        # Deleting field 'Scenario.boat_use_max'
        db.delete_column(u'scenarios_scenario', 'boat_use_max')

        # Deleting field 'Scenario.coral_cover'
        db.delete_column(u'scenarios_scenario', 'coral_cover')

        # Deleting field 'Scenario.coral_cover_min'
        db.delete_column(u'scenarios_scenario', 'coral_cover_min')

        # Deleting field 'Scenario.coral_cover_max'
        db.delete_column(u'scenarios_scenario', 'coral_cover_max')

        # Deleting field 'Scenario.coral_soft'
        db.delete_column(u'scenarios_scenario', 'coral_soft')

        # Deleting field 'Scenario.coral_soft_min'
        db.delete_column(u'scenarios_scenario', 'coral_soft_min')

        # Deleting field 'Scenario.coral_soft_max'
        db.delete_column(u'scenarios_scenario', 'coral_soft_max')

        # Deleting field 'Scenario.depth_mean'
        db.delete_column(u'scenarios_scenario', 'depth_mean')

        # Deleting field 'Scenario.depth_mean_min'
        db.delete_column(u'scenarios_scenario', 'depth_mean_min')

        # Deleting field 'Scenario.depth_mean_max'
        db.delete_column(u'scenarios_scenario', 'depth_mean_max')

        # Deleting field 'Scenario.divefish_overlap'
        db.delete_column(u'scenarios_scenario', 'divefish_overlap')

        # Deleting field 'Scenario.divefish_overlap_min'
        db.delete_column(u'scenarios_scenario', 'divefish_overlap_min')

        # Deleting field 'Scenario.divefish_overlap_max'
        db.delete_column(u'scenarios_scenario', 'divefish_overlap_max')

        # Deleting field 'Scenario.mooring_desc'
        db.delete_column(u'scenarios_scenario', 'mooring_desc')

        # Deleting field 'Scenario.mooring_desc_input'
        db.delete_column(u'scenarios_scenario', 'mooring_desc_input')

        # Deleting field 'Scenario.reccom_fish'
        db.delete_column(u'scenarios_scenario', 'reccom_fish')

        # Deleting field 'Scenario.reccom_fish_min'
        db.delete_column(u'scenarios_scenario', 'reccom_fish_min')

        # Deleting field 'Scenario.reccom_fish_max'
        db.delete_column(u'scenarios_scenario', 'reccom_fish_max')

        # Deleting field 'Scenario.sponge'
        db.delete_column(u'scenarios_scenario', 'sponge')

        # Deleting field 'Scenario.sponge_min'
        db.delete_column(u'scenarios_scenario', 'sponge_min')

        # Deleting field 'Scenario.sponge_max'
        db.delete_column(u'scenarios_scenario', 'sponge_max')

        # Deleting field 'Scenario.watersport_use'
        db.delete_column(u'scenarios_scenario', 'watersport_use')

        # Deleting field 'Scenario.watersport_use_min'
        db.delete_column(u'scenarios_scenario', 'watersport_use_min')

        # Deleting field 'Scenario.watersport_use_max'
        db.delete_column(u'scenarios_scenario', 'watersport_use_max')


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
            'acerv_area': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'acropora_pa': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'anchor_density': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'anchor_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'anchorage': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'art_area': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'boat_use': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'comfish_use': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'coral_bleach': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_cover': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_density': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_disease': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_resilience': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'coral_richness': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_soft': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'depth_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'depth_mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'depth_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'divefish_overlap': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'extdive_use': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impacted': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'injury_site': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'inlet_distance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'large_live_coral': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mooring_buoy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mooring_density': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mooring_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'outfall_distance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pier_distance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pillar_presence': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_art': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_reef': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_sand': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_sg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reccom_fish': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'recfish_use': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reef_area': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reef_fish_density': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reef_fish_richness': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'research_use': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sand_area': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scuba_use': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sg_area': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shore_distance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'spear_use': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sponge': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_use': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unique_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'watersport_use': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'scenarios.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'acropora_pa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'acropora_pa_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'anchor_desc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'anchor_desc_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'anchorage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'anchorage_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'boat_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'boat_use_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'boat_use_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'scenarios_scenario_related'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'coral_bleach': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coral_bleach_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_bleach_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_cover': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coral_cover_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_cover_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_density': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coral_density_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_density_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_disease': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coral_disease_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_disease_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_resilience': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coral_resilience_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_resilience_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_richness': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coral_richness_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_richness_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_soft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coral_soft_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coral_soft_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'depth_mean': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'depth_mean_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'depth_mean_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'divefish_overlap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'divefish_overlap_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'divefish_overlap_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'extdive_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'extdive_use_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'extdive_use_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_dissolved': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'geometry_final_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'grid_cells': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impacted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'impacted_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'injury_site': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'injury_site_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'inlet_distance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'inlet_distance_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'inlet_distance_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'large_live_coral': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'large_live_coral_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mooring_buoy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mooring_buoy_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mooring_desc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mooring_desc_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'outfall_distance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'outfall_distance_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'outfall_distance_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pier_distance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pier_distance_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pier_distance_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pillar_presence': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pillar_presence_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_art': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prcnt_art_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_art_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_reef': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prcnt_reef_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_reef_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_sand': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prcnt_sand_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_sand_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_sg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prcnt_sg_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'prcnt_sg_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reccom_fish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reccom_fish_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reccom_fish_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'recfish_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recfish_use_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'recfish_use_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reef_fish_density': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reef_fish_density_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reef_fish_density_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reef_fish_richness': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reef_fish_richness_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reef_fish_richness_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'satisfied': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'scuba_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scuba_use_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'scuba_use_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'scenarios_scenario_related'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.Group']"}),
            'shore_distance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shore_distance_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shore_distance_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'spear_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'spear_use_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'spear_use_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sponge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sponge_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sponge_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_use_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_use_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'scenarios_scenario_related'", 'to': u"orm['auth.User']"}),
            'watersport_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'watersport_use_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'watersport_use_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['scenarios']