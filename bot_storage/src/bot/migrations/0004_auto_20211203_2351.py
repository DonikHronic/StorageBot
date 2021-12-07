# Generated by Django 3.2.9 on 2021-12-03 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20211202_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='telegram_id',
        ),
        migrations.AddField(
            model_name='baseuser',
            name='telegram_id',
            field=models.PositiveIntegerField(null=True, unique=True, verbose_name='Telegram ID'),
        ),
    ]
