# Generated by Django 5.1.1 on 2024-09-09 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("email", models.EmailField(max_length=254)),
                ("full_name", models.CharField(max_length=255)),
                ("comment", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("subject", models.CharField(max_length=255)),
                ("body", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Mailing",
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
                ("start_date", models.DateTimeField()),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("daily", "Ежедневно"),
                            ("weekly", "Еженедельно"),
                            ("monthly", "Ежемесячно"),
                        ],
                        max_length=10,
                    ),
                ),
                ("status", models.CharField(default="created", max_length=10)),
                ("clients", models.ManyToManyField(to="mailings.client")),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailings.message",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MailingAttempt",
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
                ("status", models.CharField(max_length=10)),
                ("response", models.TextField()),
                ("attempt_date", models.DateTimeField(auto_now_add=True)),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailings.mailing",
                    ),
                ),
            ],
        ),
    ]
