# Generated by Django 3.2.9 on 2021-12-04 18:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bot", "0004_auto_20211203_2351"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="baseuser",
            name="email",
        ),
    ]
