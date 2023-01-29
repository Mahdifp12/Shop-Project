from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from product_module.models import Product
from .serializer import ProductSerializer


# Create your views here.


class ProductApiList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        all_product = Product.objects.all()
        serializer = ProductSerializer(all_product, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
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
