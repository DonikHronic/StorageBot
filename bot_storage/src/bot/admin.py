from django.contrib import admin
from django.utils.safestring import mark_safe

from src.bot.models import BaseUser, Client, Employee, SecretKey, Product, Cart, Ticket


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
	"""Custom user"""

	list_display = ('id', 'fullname', 'username', 'phone_number')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	"""Company clients"""

	list_display = ('id', 'user', 'cart', 'telegram_id')
	list_display_links = ('id', 'user', 'telegram_id')
	search_fields = ('telegram_id',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	"""Company employees"""

	list_display = ('id', 'user')
	list_display_links = ('id', 'user')


@admin.register(SecretKey)
class SecretKeyAdmin(admin.ModelAdmin):
	"""Secret keys for secure company datas"""

	list_display = ('id', 'key', 'employee')
	list_display_links = ('id', 'key', 'employee')
	search_fields = ('employee__name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	"""Products in stock"""

	list_display = ('id', 'name', 'description', 'get_image')
	list_display_links = ('id', 'name')
	search_fields = ('name',)
	save_on_top = True
	save_as = True

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.preview.url} width="150">')

	get_image.short_description = 'Изображение'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
	"""Products cart for make order"""
	pass


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	"""Tickets(Orders) from telegram bot"""

	list_display = ('id', 'client', 'total_price', 'status')
	list_display_links = ('id', 'client', 'total_price', 'status')
	list_filter = ('status',)
	save_as = True
	save_on_top = True
