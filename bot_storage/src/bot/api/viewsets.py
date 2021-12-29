from rest_framework import generics, views, status, parsers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.bot.api.permissions import IsOwnerProfileOrReadOnly
from src.bot.api.serializers import (
	ProductSerializer,
	EmployeeSerializer,
	BaseUserSerializer,
	CartItemSerializer
)
from src.bot.models import Product, Employee, BaseUser, Client, Cart, CartItems


class EmployeeProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]
	parser_classes = (parsers.MultiPartParser,)


class EmployeeRegistration(views.APIView):
	def post(self, request, *args, **kwargs):
		serializer = BaseUserSerializer(data=request.data)
		role = request.data.get('role')
		del request.data['role']
		if serializer.is_valid() and role == BaseUser.Role.E:
			user = BaseUser(**request.data)
			user.set_password(request.data['password'])
			user.save()
			employee = Employee(user_id=user.id)
			employee.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientRegistration(views.APIView):
	def post(self, request, *args, **kwargs):
		serializer = BaseUserSerializer(data=request.data)
		role = request.data.get('role')
		del request.data['role']
		if serializer.is_valid() and role == BaseUser.Role.C:
			user = BaseUser(**request.data)
			cart = Cart()
			cart.save()
			user.set_password(request.data['password'])
			user.save()
			employee = Client(user_id=user.id, cart_id=cart.id)
			employee.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListCreateView(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [IsAuthenticated]
	parser_classes = (parsers.MultiPartParser,)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [IsAuthenticated]
	parser_classes = (parsers.MultiPartParser,)


@api_view(['GET'])
def get_user_cart(request):
	try:
		cart = request.user.client.cart_id
		cart_items = CartItems.objects.filter(cart_id=cart)
		serializer = CartItemSerializer(cart_items, many=True)
		print(cart_items)
		return Response(serializer.data)
	except AttributeError as ex:
		return Response(f'Exception {ex}')


@api_view(['POST'])
def add_product_to_cart(request):
	try:
		user_cart = request.user.client.cart_id
		product_pk = request.data.get('product', None)
		count = request.data.get('count', None)

		if not (product_pk and count):
			raise

		cart = Cart.objects.get(id=user_cart)
		product = Product.objects.get(id=int(product_pk))
		cart_item = CartItems(product=product, cart=cart, count=count)
		cart_item.save()
		return Response('done')
	except AttributeError:
		return Response()


@api_view(['PUT'])
def update_product_in_cart(request):
	pass
