from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product_module.models import Product
from .serializer import ProductSerializer


class ProductApiList(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        products = Product.objects.all().order_by('-id')
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        product_data = {
            "title": request.data.get("title"),
            "category": request.data.get("category"),
            "is_active": request.data.get("is_active"),
            "price": request.data.get("price"),
            "short_description": request.data.get("short_description"),
            "description": request.data.get("description"),
            "brand": request.data.get("brand"),
            "slug": request.data.get("slug"),
            "is_delete": request.data.get("is_delete"),

        }

        serializer = ProductSerializer(data=product_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAdminUser])
def product_api_view_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
