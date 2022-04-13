from rest_framework import serializers

from src.storage.models import StorageProduct, ChangeHistory


class StorageProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = StorageProduct
		fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ChangeHistory
		fields = '__all__'
