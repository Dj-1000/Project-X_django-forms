# Generated by Django 5.0.1 on 2024-02-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
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
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.IntegerField(max_length=999999999999)),
                ("address", models.CharField(max_length=400)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
            ],
        ),
    ]
