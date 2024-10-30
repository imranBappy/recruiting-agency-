# Generated by Django 5.1.2 on 2024-10-30 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0003_alter_candidate_location"),
    ]

    operations = [
        migrations.CreateModel(
            name="CurrentLocation",
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
                ("location", models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name="candidate",
            name="currentLocation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="candition_CurrentLocation",
                to="job.currentlocation",
            ),
        ),
    ]