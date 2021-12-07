from django.urls import path

from src.bot.api import viewsets

urlpatterns = [
	path('products/', viewsets.get_products, name='products'),
	path('employee-registration/', viewsets.EmployeeRegistration.as_view(), name='employee-registration'),
	path('client-registration/', viewsets.ClientRegistration.as_view(), name='client-registration'),
	path('employee-profile/<int:pk>', viewsets.EmployeeProfileDetailView.as_view(), name='employee-profile'),
]
