# Generated by Django 3.2.9 on 2022-01-04 13:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
import utils.get_folder_path


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StorageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('image', models.ImageField(upload_to=utils.get_folder_path.image_path, verbose_name='Изображение')),
                ('change_date', models.DateTimeField(default=datetime.datetime.today, verbose_name='Дата изменения')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('price', models.FloatField(default=0, verbose_name='Цена')),
                ('url', models.SlugField(max_length=250, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Продукт на складе',
                'verbose_name_plural': 'Продукты на складе',
                'db_table': 'storage_product',
            },
        ),
        migrations.CreateModel(
            name='ChangeHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('date', models.DateTimeField(default=datetime.datetime.today, verbose_name='Дата')),
                ('action', models.CharField(choices=[('ADD', 'Добавлено'), ('USED', 'Использовано')], default='USED', max_length=15, verbose_name='Действие')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.storageproduct', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'История изменений',
                'verbose_name_plural': 'История изменений',
                'db_table': 'change_history',
            },
        ),
    ]
