# Generated by Django 4.2.7 on 2023-12-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "edc_registration",
            "0029_alter_historicalregisteredsubject_device_created_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="registeredsubject",
            options={
                "default_manager_name": "objects",
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "permissions": (
                    ("display_firstname", "Can display first name"),
                    ("display_lastname", "Can display last name"),
                    ("display_dob", "Can display DOB"),
                    ("display_identity", "Can display identity number"),
                    ("display_initials", "Can display initials"),
                ),
                "verbose_name": "Registered Subject",
                "verbose_name_plural": "Registered Subjects",
            },
        ),
        migrations.RemoveIndex(
            model_name="registeredsubject",
            name="edc_registr_identit_eb36e0_idx",
        ),
        migrations.AlterUniqueTogether(
            name="registeredsubject",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="historicalregisteredsubject",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="historicalregisteredsubject",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddField(
            model_name="registeredsubject",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="registeredsubject",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddIndex(
            model_name="registeredsubject",
            index=models.Index(
                fields=["modified", "created"], name="edc_registr_modifie_d58ae9_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="registeredsubject",
            index=models.Index(
                fields=["user_modified", "user_created"],
                name="edc_registr_user_mo_079b86_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="registeredsubject",
            index=models.Index(
                fields=["subject_identifier", "identity", "screening_identifier"],
                name="edc_registr_subject_6bb1e5_idx",
            ),
        ),
        migrations.AddConstraint(
            model_name="registeredsubject",
            constraint=models.UniqueConstraint(
                fields=("first_name", "dob", "initials", "additional_key"),
                name="edc_registration_registeredsubject_first_name_uniq",
            ),
        ),
    ]