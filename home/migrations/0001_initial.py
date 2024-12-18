# Generated by Django 5.1.2 on 2024-10-23 13:28

import django.core.validators
import utils.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Award",
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
                (
                    "img",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="CadidateRegistion",
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
                ("whatsApp", models.CharField(max_length=15)),
                ("phone", models.CharField(max_length=15)),
                ("name", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("resume", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=100)),
                ("whatsApp", models.CharField(max_length=15)),
                ("fb", models.URLField(default="#")),
                ("fb_group", models.URLField(default="#")),
                ("x", models.URLField(default="#")),
                ("linkedin", models.URLField(default="#")),
                ("youtube", models.URLField(default="#")),
                ("whatsAppLink", models.URLField(default="#")),
                ("location", models.TextField(max_length=250)),
                (
                    "qr_code",
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
            ],
        ),
        migrations.CreateModel(
            name="Serve",
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
                (
                    "img",
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
                ("title", models.CharField(max_length=100)),
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
                ("details_title", models.CharField(max_length=100)),
                ("details", models.CharField(max_length=1000)),
                (
                    "side_Img",
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
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("icon", models.CharField(max_length=300)),
                ("title", models.CharField(max_length=100)),
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
                ("details", models.CharField(max_length=1000)),
                (
                    "side_Img",
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
            ],
        ),
        migrations.CreateModel(
            name="Setting",
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
                ("title", models.CharField(max_length=500)),
                ("description", models.TextField(max_length=500)),
                (
                    "logo",
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
            ],
        ),
        migrations.CreateModel(
            name="Slider",
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
                (
                    "img",
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
                ("title", models.CharField(max_length=100)),
                ("subtitle", models.CharField(max_length=100)),
                ("link", models.URLField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Video",
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
                ("url", models.URLField(max_length=300)),
                ("title", models.CharField(max_length=100)),
            ],
        ),
    ]
