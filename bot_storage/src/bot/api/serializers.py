from rest_framework import serializers

from src.bot.models import Product, Employee, Client, BaseUser, CartItems, Ticket


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
    user = UserViewSerializer(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    cart = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CartItems
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
