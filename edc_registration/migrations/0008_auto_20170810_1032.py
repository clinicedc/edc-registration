# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 10:32
from __future__ import unicode_literals

import _socket
import edc_model_fields.fields.userfield
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_registration", "0007_auto_20170321_1119")]

    operations = [
        migrations.AddField(
            model_name="registeredsubject",
            name="device_created",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name="registeredsubject",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
            ),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="user_created",
            field=edc_model_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="user_modified",
            field=edc_model_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
    ]
