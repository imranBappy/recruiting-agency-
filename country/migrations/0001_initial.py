# Generated by Django 5.1.2 on 2024-10-22 17:34

import django.core.validators
import django.utils.timezone
import utils.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                (
                    "banner",
                    models.FileField(
                        upload_to="general/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "jpeg", "png"]
                            ),
                            utils.validator.validate_file_size,
                        ],
                    ),
                ),
                (
                    "flag",
                    models.FileField(
                        upload_to="general/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "jpeg", "png", "svg"]
                            ),
                            utils.validator.validate_file_size,
                        ],
                    ),
                ),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "continent",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("asia", "Asia"),
                            ("europe", "Europe"),
                            ("middleEast ", "Middle East"),
                        ],
                        max_length=250,
                        null=True,
                    ),
                ),
            ],
        ),
    ]
