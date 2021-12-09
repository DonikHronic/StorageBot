from django.urls import path

from src.bot.api import viewsets

urlpatterns = [
	path('products/', viewsets.ProductListCreateView.as_view(), name='products'),
	path('products/<int:pk>', viewsets.ProductDetailView.as_view(), name='product-detail'),
	path('employee-registration/', viewsets.EmployeeRegistration.as_view(), name='employee-registration'),
	path('client-registration/', viewsets.ClientRegistration.as_view(), name='client-registration'),
	path('employee-profile/<int:pk>', viewsets.EmployeeProfileDetailView.as_view(), name='employee-profile'),
]
