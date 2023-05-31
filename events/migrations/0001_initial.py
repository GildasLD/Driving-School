# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day",
                    models.DateField(
                        help_text="Day of the event", verbose_name="Day of the event"
                    ),
                ),
                (
                    "start_time",
                    models.TimeField(
                        help_text="Starting time", verbose_name="Starting time"
                    ),
                ),
                (
                    "end_time",
                    models.TimeField(help_text="Final time", verbose_name="Final time"),
                ),
                (
                    "notes",
                    models.TextField(
                        blank=True,
                        help_text="Textual Notes",
                        null=True,
                        verbose_name="Textual Notes",
                    ),
                ),
            ],
            options={
                "verbose_name": "Scheduling",
                "verbose_name_plural": "Scheduling",
            },
        ),
    ]
