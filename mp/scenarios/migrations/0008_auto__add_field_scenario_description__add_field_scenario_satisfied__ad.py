# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Scenario.description'
        db.add_column(u'scenarios_scenario', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.satisfied'
        db.add_column(u'scenarios_scenario', 'satisfied',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Scenario.active'
        db.add_column(u'scenarios_scenario', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Scenario.description'
        db.delete_column(u'scenarios_scenario', 'description')

        # Deleting field 'Scenario.satisfied'
        db.delete_column(u'scenarios_scenario', 'satisfied')

        # Deleting field 'Scenario.active'
        db.delete_column(u'scenarios_scenario', 'active')


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
            'AUSPATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Boundary': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'COA2005': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'COA2015': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'COAID': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Comments_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ER_Code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'GAP1_Acres': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'GAP1_PC': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'GAP2_Acres': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'GAP2_PCT': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'GAP3_Acres': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'GAP3_PCT': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'GAP4_Acres': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'GAP4_PCT': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Hex_ID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'MarxanEcor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'MarxanStat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Marxan_SIn': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'GridCell'},
            'PVT_Acres': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'PVT_PCT': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Perm_Mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Raw_SIndex': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Resist_Mea': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'SGCore': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SHAPE_Area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'SHAPE_Leng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'TNC': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'coa_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ecoregion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ecoregion_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tcd_mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'unique_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'scenarios.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'scenarios_scenario_related'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ecoregion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ecoregion_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_dissolved': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'geometry_final_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'grid_cells': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'satisfied': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'scenarios_scenario_related'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'scenarios_scenario_related'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['scenarios']