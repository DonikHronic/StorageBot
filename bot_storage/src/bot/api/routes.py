from django.urls import path

from src.bot.api import viewsets

urlpatterns = [
	path('products/', viewsets.get_products, name='products')
]
