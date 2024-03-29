# Generated by Django 3.2.9 on 2022-01-02 18:00

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bot", "0010_remove_baseuser_is_employee"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="baseuser",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.FloatField(default=0, verbose_name="Цена"),
        ),
    ]
