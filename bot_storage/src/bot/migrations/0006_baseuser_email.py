# Generated by Django 3.2.9 on 2021-12-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bot', '0005_remove_baseuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
    ]
