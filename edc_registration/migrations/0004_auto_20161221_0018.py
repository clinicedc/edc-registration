# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 00:18
from __future__ import unicode_literals

import edc_utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_registration", "0003_registeredsubject_subject_type")]

    operations = [
        migrations.AlterField(
            model_name="registeredsubject",
            name="subject_identifier",
            field=models.CharField(
                max_length=50, unique=True, verbose_name="Subject Identifier"
            ),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="subject_identifier_as_pk",
            field=models.CharField(
                default=edc_utils.get_uuid,
                editable=False,
                max_length=50,
                verbose_name="Subject Identifier as pk",
            ),
        ),
    ]
