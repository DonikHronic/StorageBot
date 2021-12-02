from datetime import datetime

from django.db import models
from django.urls import reverse

from utils.get_folder_path import image_path


class Product(models.Model):
	"""Product"""

	name = models.CharField('Название', max_length=150)
	image = models.ImageField('Избражение', upload_to=image_path)
	change_date = models.DateTimeField('Дата изменения', default=datetime.today)
	count = models.PositiveIntegerField('Количество', default=0)
	url = models.SlugField('URL', max_length=250)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product_detail', kwargs={'slug': self.url})

	class Meta:
		db_table = 'storage_product'
		verbose_name = 'Продукт на складе'
		verbose_name_plural = 'Продукты на складе'


class ChangeHistory(models.Model):
	"""Change history"""

	class Action(models.TextChoices):
		ADD = 'ADD', 'Добавлено'
		USED = 'USED', 'Использовано'

	product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
	count = models.PositiveIntegerField('Количество', default=0)
	date = models.DateTimeField('Дата', default=datetime.today)
	action = models.CharField('Действие', choices=Action.choices, default=Action.USED, max_length=15)

	def __str__(self):
		return f'{self.product} - {self.action} - {self.count}'

	class Meta:
		db_table = 'change_history'
		verbose_name = 'История изменений'
		verbose_name_plural = 'История изменений'
