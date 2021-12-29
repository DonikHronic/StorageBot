from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.urls import reverse

from src.bot.UserManager import UserManager
from utils.get_folder_path import image_path


class BaseUser(AbstractBaseUser, PermissionsMixin):
	"""Custom user for control"""

	class Role(models.TextChoices):
		E = 'E', 'Employee'
		C = 'C', 'Client'

	username = models.CharField('Пользователь', max_length=25, unique=True)
	email = models.EmailField('Email', unique=True, null=True, blank=True)
	phone_number = models.CharField('Номер телефона', max_length=15, null=True, blank=True)
	fullname = models.CharField('Полное имя', max_length=150)
	telegram_id = models.PositiveIntegerField('Telegram ID', unique=True, null=True)

	date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
	is_active = models.BooleanField('is_active', default=True)
	is_staff = models.BooleanField('is_staff', default=False)
	user_photo = models.ImageField(upload_to='users_photos/', null=True, blank=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.fullname

	def get_full_name(self):
		return self.username

	def get_short_name(self):
		return self.username

	class Meta:
		db_table = 'user'
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Employee(models.Model):
	"""Company employees"""

	user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='employee')

	def __str__(self):
		return f'{self.user}'

	class Meta:
		db_table = 'employee'
		verbose_name = 'Сотрудник'
		verbose_name_plural = 'Сотрудники'


class Client(models.Model):
	"""Company clients"""

	user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='client')
	cart = models.ForeignKey('Cart', on_delete=models.SET_NULL, null=True, blank=True, related_name='client_cart')

	def __str__(self):
		return f'{self.user}'

	class Meta:
		db_table = 'client'
		verbose_name = 'Клиент'
		verbose_name_plural = 'Клиенты'


class SecretKey(models.Model):
	"""Secret keys for secure company datas"""

	key = models.CharField('Секретный ключ', max_length=20)
	employee = models.OneToOneField(
		Employee, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сотрудник'
	)

	def __str__(self):
		return f'{self.key} => {self.employee}'

	class Meta:
		db_table = 'secret_key'
		verbose_name = 'Секретный ключ'
		verbose_name_plural = 'Секретные ключи'


class Product(models.Model):
	"""Products in stock"""

	name = models.CharField('Название', max_length=150)
	image = models.ImageField('Изображение', upload_to=image_path)
	description = models.TextField('Описание', max_length=5000)
	url = models.SlugField('Ссылка', unique=True, max_length=250)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product_detail', kwargs={'slug': self.url})

	class Meta:
		db_table = 'product'
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'


class Cart(models.Model):
	"""Products cart for make order"""

	items = models.ManyToManyField(Product, verbose_name='Продукты', through='CartItems')

	def __str__(self):
		return f'{self.items}'

	class Meta:
		db_table = 'cart'
		verbose_name = 'Корзина'
		verbose_name_plural = 'Корзины'


class CartItems(models.Model):
	"""Intermediary model for cart items"""

	product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
	count = models.PositiveIntegerField('Количество', default=1)

	def __str__(self):
		return f'{self.product} - {self.count}'

	class Meta:
		db_table = 'cart_items'
		verbose_name = 'Элемент корзины'
		verbose_name_plural = 'Элементы корзины'


class Ticket(models.Model):
	"""Tickets(Orders) from telegram bot"""

	class Statuses(models.TextChoices):
		IN_PROCESS = 'IN_PROCESS', 'В обработке'
		ACCEPTED = 'ACCEPTED', 'Принята'
		IN_PURCHASE = 'IN_PURCHASE', 'В процессе закупа'
		PREPARE_FOR_SHIPMENT = 'PREPARE_FOR_SHIPMENT', 'Подготовка к отправке'
		SUBMITTED = 'SUBMITTED', 'Отправлена'
		COMPLETED = 'COMPLETED', 'Завершена'

	client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Клиент')
	products = models.ManyToManyField(Product, verbose_name='Продукты')
	total_price = models.FloatField('Окончательная цена', default=0)
	location = models.CharField('Локация доставки', max_length=150)
	status = models.CharField('Статус', choices=Statuses.choices, default=Statuses.IN_PROCESS, max_length=25)

	def __str__(self):
		return f'{self.total_price}'

	class Meta:
		db_table = 'ticket'
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'
