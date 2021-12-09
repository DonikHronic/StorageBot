from rest_framework import serializers

from src.bot.models import Product, Employee, Client, BaseUser


class BaseUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseUser
		fields = ['username', 'password']


class UserViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseUser
		fields = ['id', 'fullname', 'username', 'user_photo', 'email', 'phone_number', 'telegram_id']


class EmployeeSerializer(serializers.ModelSerializer):
	user = UserViewSerializer(read_only=True)

	class Meta:
		model = Employee
		fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
	user = serializers.StringRelatedField(read_only=True)

	class Meta:
		model = Client
		fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'
