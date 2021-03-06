# Generated by Django 2.2.1 on 2019-05-29 16:05

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AOI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('manipulators', models.TextField(blank=True, help_text='csv list of manipulators to be applied', null=True, verbose_name='Manipulator List')),
                ('geometry_orig', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=3857, verbose_name='Original Polygon Geometry')),
                ('geometry_final', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=3857, verbose_name='Final Polygon Geometry')),
                ('description', models.TextField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='drawing_aoi_related', to='contenttypes.ContentType')),
                ('sharing_groups', models.ManyToManyField(blank=True, editable=False, null=True, related_name='drawing_aoi_related', to='auth.Group', verbose_name='Share with the following groups')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drawing_aoi_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
