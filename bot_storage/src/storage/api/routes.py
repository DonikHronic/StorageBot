from django.urls import path

from src.storage.api import viewsets

urlpatterns = [
    path('products/', viewsets.StorageProductListCreateView.as_view(), name='products'),
    path('products/<int:pk>/', viewsets.StorageProductDetailView.as_view(), name='products-detail'),
    path('update-storage/', viewsets.change_storage, name='update-storage'),
    path('history/', viewsets.get_history, name='history'),
]
