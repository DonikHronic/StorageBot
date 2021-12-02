# Generated by Django 3.2.9 on 2021-12-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='user_id',
        ),
        migrations.AddField(
            model_name='client',
            name='telegram_id',
            field=models.PositiveIntegerField(null=True, unique=True, verbose_name='Telegram ID'),
        ),
    ]