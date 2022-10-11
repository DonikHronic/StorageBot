from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, views, status, parsers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.bot.api.permissions import IsOwnerProfileOrReadOnly
from src.bot.api.serializers import (
    ProductSerializer,
    EmployeeSerializer,
    BaseUserSerializer,
    CartItemSerializer,
    TicketSerializer,
)
from src.bot.models import Product, Employee, BaseUser, Client, Cart, CartItems, Ticket


class EmployeeProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Employee profile. Account settings
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]
    parser_classes = (parsers.MultiPartParser,)


class EmployeeRegistration(views.APIView):
    """
    Registration Employees
    Take data as:
    {
        "username": "username", -> required
        "password": "some_password", -> required
        "role": "E" -> required (needed to determine the type of user)
    }
    """

    def post(self, request, *args, **kwargs):
        serializer = BaseUserSerializer(data=request.data)
        data = {key: val for key, val in request.data.items()}
        try:
            data["telegram_id"] = int(data["telegram_id"])
        except KeyError:
            pass
        role = data["role"]
        del data["role"]
        if serializer.is_valid() and role == BaseUser.Role.E:
            user = BaseUser(**data)
            user.set_password(request.data["password"])
            user.save()
            employee = Employee(user_id=user.id)
            employee.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientRegistration(views.APIView):
    """
    Registration Clients
    Take data as:
    {
        "username": "username", -> required
        "password": "some_password", -> required
        "role": "C" -> required (needed to determine the type of user)
    }
    """

    def post(self, request, *args, **kwargs):
        serializer = BaseUserSerializer(data=request.data)
        data = {key: val for key, val in request.data.items()}
        try:
            data["telegram_id"] = int(data["telegram_id"])
        except KeyError:
            pass
        role = data["role"]
        del data["role"]
        if serializer.is_valid() and role == BaseUser.Role.C:
            user = BaseUser(**data)
            cart = Cart()
            cart.save()
            user.set_password(request.data["password"])
            user.save()
            employee = Client(user_id=user.id, cart_id=cart.id)
            employee.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListCreateView(generics.ListCreateAPIView):
    """
    Product View
    Create new Product or return Products List
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (parsers.MultiPartParser,)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Product Detail View
    Allows you to view and modify Product information
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (parsers.MultiPartParser,)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_cart(request) -> Response:
    """
    Returns a JSON object containing a list and count of products in the cart of a specific user
    """
    try:
        cart = request.user.client.cart_id
        cart_items = CartItems.objects.filter(cart_id=cart)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)
    except AttributeError as ex:
        return Response([f"Exception found: {ex}"], status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_product_to_cart(request) -> Response:
    """
    Add product in user cart
    """
    try:
        user_cart = request.user.client.cart_id
        product_id = request.data.get("product", None)
        count = request.data.get("count", 1)

        if not product_id:
            raise ValueError("Product parameter is required")

        check_cart = CartItems.objects.filter(cart_id=user_cart, product_id=product_id)
        if check_cart:
            cart_item = check_cart[0]
            cart_item.count = count
            cart_item.save()
            return Response(["Product added to cart"], status=status.HTTP_202_ACCEPTED)

        cart = Cart.objects.get(id=user_cart)
        product = Product.objects.get(id=int(product_id))
        cart_item = CartItems(product=product, cart=cart, count=count)
        cart_item.save()
        return Response(["Product added to cart"], status=status.HTTP_201_CREATED)
    except AttributeError as ex:
        return Response([f"Exception found: {ex}"], status=status.HTTP_400_BAD_REQUEST)
    except ValueError as ex:
        return Response([f"Exception found. {ex}"], status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist as ex:
        return Response([f"Exception found: {ex}"], status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_product_in_cart(request, pk: int) -> Response:
    """
    Update product information in user cart
    :param request: Must contain count in request body
    :param pk: Product ID
    :return:
    """

    try:
        count = request.data.get("count", None)

        if not count:
            raise ValueError("Count parameter is required")

        item = CartItems.objects.get(id=pk)
        item.count = count
        item.save()
        return Response(["Product updated"], status=status.HTTP_202_ACCEPTED)

    except AttributeError as ex:
        return Response([f"Exception found: {ex}"], status=status.HTTP_400_BAD_REQUEST)
    except ValueError as ex:
        return Response(f"Exception found: {ex}", status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist as ex:
        return Response([f"Exception found: {ex}"], status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, pk: int) -> Response:
    """
    Delete product from cart by Product ID
    :param request:
    :param pk: Product ID
    :return:
    """
    try:
        cart = request.user.client.cart_id
        item = CartItems.objects.get(cart_id=cart, product_id=pk)
        item.delete()

        return Response(["Product removed"], status=status.HTTP_200_OK)
    except AttributeError as ex:
        return Response([f"Exception found: {ex}"], status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response(
            ["Your cart does not have this product"], status=status.HTTP_404_NOT_FOUND
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def clear_cart(request) -> Response:
    """
    Clear user cart
    """
    try:
        cart = request.user.client.cart_id
        items = CartItems.objects.filter(cart_id=cart)

        for item in items:
            item.delete()

        return Response(["Cart cleared"], status=status.HTTP_200_OK)

    except AttributeError as ex:
        return Response([f"Exception found: {ex}"], status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def make_order(request) -> Response:
    try:
        user = request.user.client
        cart_items = CartItems.objects.filter(cart_id=user.cart_id)
        location = request.data.get("location", "default")
        total_price = get_total_price(cart_items)
        products = [item.product for item in cart_items]

        description = ""
        for item in cart_items:
            description += f"Продукт: {item.product.name} в кол-ве {item.count}шт\n"

        ticket = Ticket(
            client=user, total_price=total_price, location=location, detail=description
        )
        ticket.save()
        ticket.products.add(*products)
        ticket.save()

        for item in cart_items:
            item.delete()

        return Response(["Order created"], status=status.HTTP_201_CREATED)
    except AttributeError as ex:
        return Response([f"Exception found: {ex}"], status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_orders(request):
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_my_orders(request):
    try:
        user = request.user.client
        tickets = Ticket.objects.filter(client=user)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except AttributeError as ex:
        return Response([f"Exception found: {ex}"], status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_status_list(request) -> Response:
    return Response(Ticket.Statuses.choices, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_status(request) -> Response:
    try:
        order_status = request.data.get("status", None)
        order = request.data.get("order", None)

        if not order_status:
            raise ValueError("Status is required")

        if not order:
            raise ValueError("Order ID is required")

        if order_status not in Ticket.Statuses.names:
            raise ValueError("Invalid status")

        ticket = Ticket.objects.get(id=order)
        ticket.status = order_status
        ticket.save()

        return Response(["Status updated"], status=status.HTTP_202_ACCEPTED)

    except AttributeError as ex:
        return Response([f"Exception found: {ex}"], status=status.HTTP_400_BAD_REQUEST)
    except ValueError as ex:
        return Response(
            [f"Invalid data in request: {ex}"], status=status.HTTP_400_BAD_REQUEST
        )
    except ObjectDoesNotExist:
        return Response(
            [f'Order with ID {request.data.get("order", None)}, does not exist'],
            status=status.HTTP_400_BAD_REQUEST,
        )


def get_total_price(items) -> float:
    return sum([item.product.price * item.count for item in items])
