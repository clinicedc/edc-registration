# Generated by Django 2.1.7 on 2019-02-26 23:48

import uuid

import _socket
import django.core.validators
import django.db.models.deletion
import django_audit_fields.fields.uuid_auto_field
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.firstname_field
import django_crypto_fields.fields.identity_field
import django_crypto_fields.fields.lastname_field
import django_revision.revision_field
import edc_model_fields.fields.date_estimated
import edc_model_fields.fields.hostname_modification_field
import edc_model_fields.fields.identity_type_field
import edc_model_fields.fields.userfield
import edc_utils
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sites", "0002_alter_domain_unique"),
        ("edc_registration", "0015_auto_20181006_2257"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalRegisteredSubject",
            fields=[
                (
                    "created",
                    models.DateTimeField(blank=True, default=edc_utils.date.get_utcnow),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, default=edc_utils.date.get_utcnow),
                ),
                (
                    "user_created",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    edc_model_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "subject_identifier",
                    models.CharField(
                        db_index=True, max_length=50, verbose_name="Subject Identifier"
                    ),
                ),
                (
                    "subject_identifier_as_pk",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                (
                    "subject_identifier_aka",
                    models.CharField(
                        editable=False,
                        help_text="track a previously allocated identifier.",
                        max_length=50,
                        null=True,
                        verbose_name="Subject Identifier a.k.a",
                    ),
                ),
                (
                    "first_name",
                    django_crypto_fields.fields.firstname_field.FirstnameField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                    ),
                ),
                (
                    "last_name",
                    django_crypto_fields.fields.lastname_field.LastnameField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        verbose_name="Last name",
                    ),
                ),
                (
                    "initials",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Ensure initials consist of letters only in upper case, no spaces.",
                                regex="^[A-Z]{2,3}$",
                            )
                        ],
                    ),
                ),
                (
                    "dob",
                    models.DateField(
                        help_text="Format is YYYY-MM-DD",
                        null=True,
                        verbose_name="Date of birth",
                    ),
                ),
                (
                    "is_dob_estimated",
                    edc_model_fields.fields.date_estimated.IsDateEstimatedField(
                        choices=[
                            ("-", "No"),
                            ("D", "Yes, estimated the Day"),
                            ("MD", "Yes, estimated Month and Day"),
                            ("YMD", "Yes, estimated Year, Month and Day"),
                        ],
                        help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                        max_length=25,
                        null=True,
                        verbose_name="Is date of birth estimated?",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=1,
                        null=True,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "subject_consent_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "registration_identifier",
                    models.CharField(blank=True, max_length=36, null=True),
                ),
                (
                    "sid",
                    models.CharField(blank=True, max_length=15, null=True, verbose_name="SID"),
                ),
                (
                    "subject_type",
                    models.CharField(blank=True, max_length=25, null=True),
                ),
                (
                    "relative_identifier",
                    models.CharField(
                        blank=True,
                        help_text="For example, mother's identifier, if available / appropriate",
                        max_length=36,
                        null=True,
                        verbose_name="Identifier of immediate relation",
                    ),
                ),
                (
                    "identity",
                    django_crypto_fields.fields.identity_field.IdentityField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                    ),
                ),
                (
                    "identity_or_pk",
                    models.CharField(
                        db_index=True,
                        default=edc_utils.get_uuid,
                        editable=False,
                        max_length=75,
                        verbose_name="identity or pk",
                    ),
                ),
                (
                    "identity_type",
                    edc_model_fields.fields.identity_type_field.IdentityTypeField(
                        blank=True,
                        choices=[
                            ("OMANG", "Omang"),
                            ("DRIVERS", "Driver's License"),
                            ("PASSPORT", "Passport"),
                            ("OMANG_RCPT", "Omang Receipt"),
                            ("OTHER", "Other"),
                        ],
                        max_length=15,
                        null=True,
                        verbose_name="What type of identity number is this?",
                    ),
                ),
                (
                    "screening_identifier",
                    models.CharField(blank=True, max_length=36, null=True),
                ),
                ("screening_datetime", models.DateTimeField(blank=True, null=True)),
                ("screening_age_in_years", models.IntegerField(blank=True, null=True)),
                ("registration_datetime", models.DateTimeField(blank=True, null=True)),
                ("randomization_datetime", models.DateTimeField(blank=True, null=True)),
                (
                    "registration_status",
                    models.CharField(
                        blank=True,
                        max_length=25,
                        null=True,
                        verbose_name="Registration status",
                    ),
                ),
                ("consent_datetime", models.DateTimeField(blank=True, null=True)),
                (
                    "comment",
                    models.TextField(
                        blank=True, max_length=250, null=True, verbose_name="Comment"
                    ),
                ),
                (
                    "additional_key",
                    models.CharField(
                        default=None,
                        editable=False,
                        help_text="A uuid (or some other text value) to be added to bypass the unique constraint of just firstname, initials, and dob.The default constraint proves limiting since the source model usually has some other attribute in additional to first_name, initials and dob which is not captured in this model",
                        max_length=36,
                        null=True,
                        verbose_name="-",
                    ),
                ),
                (
                    "dm_comment",
                    models.CharField(
                        editable=False,
                        max_length=150,
                        null=True,
                        verbose_name="Data Management comment",
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Registered Subject",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        )
    ]
