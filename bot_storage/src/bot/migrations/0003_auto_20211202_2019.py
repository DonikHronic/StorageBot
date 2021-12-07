# Generated by Django 3.2.9 on 2021-12-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20211201_0948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('IN_PROCESS', 'В обработке'), ('ACCEPTED', 'Принята'), ('IN_PURCHASE', 'В процессе закупа'), ('PREPARE_FOR_SHIPMENT', 'Подготовка к отправке'), ('SUBMITTED', 'Отправлена'), ('COMPLETED', 'Завершена')], default='IN_PROCESS', max_length=25, verbose_name='Статус'),
        ),
    ]