from rest_framework import generics, views, status, parsers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.bot.api.permissions import IsOwnerProfileOrReadOnly
from src.bot.api.serializers import ProductSerializer, EmployeeSerializer, BaseUserSerializer
from src.bot.models import Product, Employee, BaseUser, Client


class EmployeeProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]
	parser_classes = (parsers.MultiPartParser,)


class EmployeeRegistration(views.APIView):
	def post(self, request, *args, **kwargs):
		serializer = BaseUserSerializer(data=request.data)
		role = request.data.get('role')
		if serializer.is_valid() and role == BaseUser.Role.E:
			user = BaseUser(**request.data)
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
			user.save()
			employee = Client(user_id=user.id)
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
