# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import edc_model_fields.fields.hostname_modification_field
import edc_model_fields.fields.userfield
import edc_utils


class Migration(migrations.Migration):

    dependencies = [("edc_registration", "0004_auto_20161221_0018")]

    operations = [
        migrations.AlterField(
            model_name="registeredsubject",
            name="created",
            field=models.DateTimeField(blank=True, default=edc_utils.date.get_utcnow),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default="mac2-2.local",
                help_text="System field. (modified on create only)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="hostname_modified",
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="identity_or_pk",
            field=models.CharField(
                default=edc_utils.get_uuid,
                editable=False,
                max_length=75,
                unique=True,
                verbose_name="identity or pk",
            ),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="modified",
            field=models.DateTimeField(blank=True, default=edc_utils.date.get_utcnow),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="relative_identifier",
            field=models.CharField(
                blank=True,
                help_text="For example, mother's identifier, if available / appropriate",
                max_length=36,
                null=True,
                verbose_name="Identifier of immediate relation",
            ),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="user_created",
            field=edc_model_fields.fields.userfield.UserField(
                blank=True, max_length=50, verbose_name="user created"
            ),
        ),
        migrations.AlterField(
            model_name="registeredsubject",
            name="user_modified",
            field=edc_model_fields.fields.userfield.UserField(
                blank=True, max_length=50, verbose_name="user modified"
            ),
        ),
    ]
