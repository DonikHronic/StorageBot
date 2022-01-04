from django.contrib import admin
from django.utils.safestring import mark_safe

from src.storage.models import StorageProduct, ChangeHistory


@admin.register(StorageProduct)
class ProductAdmin(admin.ModelAdmin):
	"""Product"""

	list_display = ('id', 'name', 'count', 'change_date', 'get_image')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'change_date')
	save_on_top = True
	save_as = True

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="150">')

	get_image.short_description = 'Изображение'


@admin.register(ChangeHistory)
class ChangeHistoryAdmin(admin.ModelAdmin):
	"""Change history"""

	list_display = ('id', 'product', 'action', 'count', 'date')
	list_display_links = ('id', 'product')
	list_filter = ('action',)
	search_fields = ('product__name',)
	save_on_top = True
	save_as = True
