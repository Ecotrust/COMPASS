# Generated by Django 2.2.1 on 2019-05-29 16:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(blank=True, max_length=255, null=True)),
                ('field_name', models.CharField(blank=True, max_length=255, null=True)),
                ('precision', models.IntegerField(blank=True, null=True)),
                ('order', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('slug_name', models.CharField(blank=True, max_length=244, null=True)),
                ('layer_type', models.CharField(choices=[('XYZ', 'XYZ'), ('WMS', 'WMS'), ('ArcRest', 'ArcRest'), ('Vector', 'Vector')], help_text='Use "XYZ" for ArcGIS tiles', max_length=50)),
                ('layer_source', models.CharField(blank=True, choices=[('featureserver', 'ArcGIS Feature Server'), ('mapserver', 'ArcGIS Map Server (tiles)'), ('ArcRest', 'ArcGIS Map Server (vector)'), ('XYZ', 'XYZ Tiles'), ('Vector', 'Vector'), ('WMS', 'WMS')], default=None, max_length=50, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('compass_instance_id', models.CharField(blank=True, default='uUvqNMGPm7axC2dD', max_length=255, null=True)),
                ('compass_service_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('shareable_url', models.BooleanField(default=True, help_text='Shareable (non-vector) layers will offer a Tiles link')),
                ('proxy_url', models.BooleanField(default=False, help_text='proxy layer url through marine planner')),
                ('arcgis_layers', models.CharField(blank=True, help_text='IDs separated by commas (no spaces)', max_length=255, null=True)),
                ('wms_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('is_sublayer', models.BooleanField(default=False)),
                ('legend', models.CharField(blank=True, help_text='Path to Legend Image file (http://somewhere.com/legend.png)', max_length=255, null=True)),
                ('legend_title', models.CharField(blank=True, help_text='If no value is entered, the layer name will be used as the Legend Title', max_length=255, null=True)),
                ('legend_subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('utfurl', models.CharField(blank=True, help_text='For XYZ MBTiles this should be the same URL as entered above, but ending with .grid.json rather than .png', max_length=255, null=True)),
                ('utfjsonp', models.BooleanField(default=False, help_text='For MBTiles, check this box')),
                ('summarize_to_grid', models.BooleanField(default=False)),
                ('filterable', models.BooleanField(default=False)),
                ('proj', models.CharField(blank=True, choices=[('EPSG:3643', 'Oregon Lambert (ODFW Default) [3643]'), ('EPSG:2992', 'Oregon Lambert (ft) [2992]'), ('EPSG:3857', 'Web Mercator [3857]'), ('EPSG:4326', 'WGS 84 [4326]'), ('ESRI:102100', 'ESRI Web Mercator WSG84'), ('ORNAD83M', 'OR Lambert Conformal Conic NAD 1983 (m)'), ('SR-ORG:45', '102113')], help_text='will be EPSG:3857, if unspecified', max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('data_overview', models.TextField(blank=True, null=True)),
                ('data_source', models.CharField(blank=True, max_length=255, null=True)),
                ('data_notes', models.TextField(blank=True, null=True)),
                ('bookmark', models.CharField(blank=True, max_length=755, null=True)),
                ('map_tiles', models.CharField(blank=True, max_length=255, null=True)),
                ('kml', models.CharField(blank=True, max_length=255, null=True)),
                ('data_download', models.CharField(blank=True, help_text='Link to download the data', max_length=255, null=True)),
                ('metadata', models.CharField(blank=True, help_text='Link to the metadata', max_length=255, null=True)),
                ('source', models.CharField(blank=True, help_text='Link to the data providers', max_length=255, null=True)),
                ('ocs', models.CharField(blank=True, help_text='Link to OCS page', max_length=255, null=True)),
                ('attribute_title', models.CharField(blank=True, help_text='If no value is entered, the layer name will be used as the header for the Attribute list (triggered on click events)', max_length=255, null=True)),
                ('compress_display', models.BooleanField(default=False)),
                ('attribute_event', models.CharField(choices=[('click', 'click'), ('mouseover', 'mouseover')], default='click', help_text="Only 'click' is available at this time", max_length=35)),
                ('lookup_field', models.CharField(blank=True, max_length=255, null=True)),
                ('vector_color', models.CharField(blank=True, help_text='Outline color represented in a hex format (e.g. #00ff00)', max_length=7, null=True)),
                ('vector_fill', models.FloatField(blank=True, help_text="Fill opacity represented by a floating point value (e.g. '.8')", null=True)),
                ('vector_graphic', models.CharField(blank=True, max_length=255, null=True)),
                ('opacity', models.FloatField(blank=True, default=0.5, null=True)),
                ('arc_rest_data_layer', models.BooleanField(default=False)),
                ('arc_rest_instance_id', models.CharField(blank=True, default='uUvqNMGPm7axC2dD', max_length=150, null=True)),
                ('arc_rest_service_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('arc_rest_out_fields', models.TextField(blank=True, default='*', help_text="comma separated list of fields to return. '*' for all fields.", null=True)),
                ('attribute_fields', models.ManyToManyField(blank=True, null=True, to='data_manager.AttributeInfo')),
            ],
        ),
        migrations.CreateModel(
            name='LookupInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=7, null=True)),
                ('dashstyle', models.CharField(choices=[('dot', 'dot'), ('dash', 'dash'), ('dashdot', 'dashdot'), ('longdash', 'longdash'), ('longdashdot', 'longdashdot'), ('solid', 'solid')], default='solid', max_length=11)),
                ('fill', models.BooleanField(default=False)),
                ('graphic', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('header_image', models.CharField(blank=True, max_length=255, null=True)),
                ('header_attrib', models.CharField(blank=True, max_length=255, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.URLField(blank=True, max_length=255, null=True)),
                ('factsheet_thumb', models.CharField(blank=True, max_length=255, null=True)),
                ('factsheet_link', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_image', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_excerpt', models.TextField(blank=True, null=True)),
                ('feature_link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TOCSubTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=150)),
                ('name', models.CharField(help_text="This field should be a 'slugified' version of Display Name (must start with a letter and should only contain letters (a-z or A-Z), digits (0-9), hyphens(-), and underscores(_))", max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('layers', models.ManyToManyField(blank=True, null=True, to='data_manager.Layer')),
            ],
        ),
        migrations.CreateModel(
            name='TOCTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=100)),
                ('name', models.CharField(help_text="This field should be a 'slugified' version of Display Name (must start with a letter and should only contain letters (a-z or A-Z), digits (0-9), hyphens(-), and underscores(_))", max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('layers', models.ManyToManyField(blank=True, null=True, to='data_manager.Layer')),
                ('subthemes', models.ManyToManyField(blank=True, null=True, to='data_manager.TOCSubTheme')),
            ],
        ),
        migrations.CreateModel(
            name='TOC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('themes', models.ManyToManyField(blank=True, null=True, to='data_manager.TOCTheme')),
            ],
        ),
        migrations.AddField(
            model_name='layer',
            name='lookup_table',
            field=models.ManyToManyField(blank=True, null=True, to='data_manager.LookupInfo'),
        ),
        migrations.AddField(
            model_name='layer',
            name='sublayers',
            field=models.ManyToManyField(blank=True, null=True, related_name='_layer_sublayers_+', to='data_manager.Layer'),
        ),
        migrations.AddField(
            model_name='layer',
            name='themes',
            field=models.ManyToManyField(blank=True, null=True, to='data_manager.Theme'),
        ),
        migrations.CreateModel(
            name='ImportEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('complete', 'Complete'), ('failed', 'Failed'), ('running', 'Running'), ('pending', 'Pending'), ('unknown', 'Unknown')], default='unknown', max_length=255)),
                ('notes', models.TextField(blank=True, default=None, null=True)),
                ('data_file', models.FileField(upload_to='data_manager_uploads/%Y/%m/%d')),
                ('user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DataNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('archived', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=255, null=True)),
                ('expected_date', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('themes', models.ManyToManyField(blank=True, null=True, to='data_manager.Theme')),
            ],
        ),
    ]
