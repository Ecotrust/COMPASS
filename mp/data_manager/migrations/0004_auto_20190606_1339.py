# Generated by Django 2.2.1 on 2019-06-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0003_layer_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='order',
            field=models.IntegerField(default=999),
        ),
        migrations.AddField(
            model_name='tocsubtheme',
            name='order',
            field=models.IntegerField(default=999),
        ),
    ]