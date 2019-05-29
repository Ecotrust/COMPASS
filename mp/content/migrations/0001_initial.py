# Generated by Django 2.2.1 on 2019-05-29 09:35

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('display_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]
