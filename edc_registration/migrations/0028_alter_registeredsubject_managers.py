# Generated by Django 4.2.1 on 2023-07-07 19:32

import edc_sites.models
from django.db import migrations

import edc_registration.models.managers


class Migration(migrations.Migration):
    dependencies = [
        ("edc_registration", "0027_alter_registeredsubject_options"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="registeredsubject",
            managers=[
                (
                    "objects",
                    edc_registration.models.managers.RegisteredSubjectManager(),
                ),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
    ]
