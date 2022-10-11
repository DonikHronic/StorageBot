from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, parsers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.storage.api.serializers import StorageProductSerializer, HistorySerializer
from src.storage.models import StorageProduct, ChangeHistory


class StorageProductListCreateView(generics.ListCreateAPIView):
    """
    Product View
    Create new Product or return Products List
    """

    queryset = StorageProduct.objects.all()
    serializer_class = StorageProductSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (parsers.MultiPartParser,)


class StorageProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Product Detail View
    Allows you to view and modify Product information
    """

    queryset = StorageProduct.objects.all()
    serializer_class = StorageProductSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (parsers.MultiPartParser,)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_storage(request):
    action = request.data.get("action", None)
    count = request.data.get("count", None)
    product_id = request.data.get("product", None)

    if action not in ChangeHistory.Action.names:
        return Response(
            ["Invalid action. Must be ADD or USED"], status=status.HTTP_400_BAD_REQUEST
        )

    if count:
        count = int(count)
    else:
        return Response(
            ["Count parameter is required"], status=status.HTTP_400_BAD_REQUEST
        )

    try:
        product = StorageProduct.objects.get(id=product_id)
        if action in ChangeHistory.Action.ADD:
            product.count += count
            product.change_date = datetime.utcnow()
            product.save()
        elif product.count < count:
            return Response(
                ["Your count could not be more then product count"],
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            product.count -= count
            product.change_date = datetime.now()
            product.save()

        history = ChangeHistory(product=product, count=count, action=action)
        history.save()

        return Response(["Storage updated"], status=status.HTTP_200_OK)

    except ObjectDoesNotExist:
        return Response(
            ["This product does not exist"], status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def get_history(request):
    objects = ChangeHistory.objects.all()
    serializer = HistorySerializer(objects, many=True)
    return Response(serializer.data)
