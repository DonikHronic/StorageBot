# Generated by Django 3.2.9 on 2021-12-13 18:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bot", "0009_alter_baseuser_managers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="baseuser",
            name="is_employee",
        ),
    ]
