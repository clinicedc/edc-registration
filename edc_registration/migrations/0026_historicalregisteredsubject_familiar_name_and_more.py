# Generated by Django 4.1.2 on 2023-01-25 00:06

from django.db import migrations
import django_crypto_fields.fields.lastname_field


class Migration(migrations.Migration):

    dependencies = [
        ("edc_registration", "0025_auto_20220914_0038"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalregisteredsubject",
            name="familiar_name",
            field=django_crypto_fields.fields.lastname_field.LastnameField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                null=True,
                verbose_name="Familiar name",
            ),
        ),
        migrations.AddField(
            model_name="historicalregisteredsubject",
            name="full_name",
            field=django_crypto_fields.fields.lastname_field.LastnameField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                null=True,
                verbose_name="Full name",
            ),
        ),
        migrations.AddField(
            model_name="registeredsubject",
            name="familiar_name",
            field=django_crypto_fields.fields.lastname_field.LastnameField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                null=True,
                verbose_name="Familiar name",
            ),
        ),
        migrations.AddField(
            model_name="registeredsubject",
            name="full_name",
            field=django_crypto_fields.fields.lastname_field.LastnameField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                null=True,
                verbose_name="Full name",
            ),
        ),
    ]
