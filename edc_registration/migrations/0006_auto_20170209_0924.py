# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_registration", "0005_auto_20170111_1809")]

    operations = [
        migrations.AlterField(
            model_name="registeredsubject",
            name="additional_key",
            field=models.CharField(
                default=None,
                editable=False,
                help_text="A uuid (or some other text value) to be added to bypass the unique constraint of just firstname, initials, and dob.The default constraint proves limiting since the source model usually has some other attribute in additional to first_name, initials and dob which is not captured in this model",
                max_length=36,
                null=True,
                verbose_name="-",
            ),
        )
    ]
