# Generated by Django 2.0.1 on 2018-01-16 13:28

from django.db import migrations
import edc_sites.models


class Migration(migrations.Migration):

    dependencies = [("edc_registration", "0011_auto_20180116_1411")]

    operations = [
        migrations.AlterModelManagers(
            name="registeredsubject",
            managers=[("on_site", edc_sites.models.CurrentSiteManager())],
        )
    ]
