# Generated by Django 2.2.1 on 2019-06-06 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0005_toctheme_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importevent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
