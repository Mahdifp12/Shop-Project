from rest_framework import serializers
from product_module.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = [
            'category',
            'brand',
            'slug',
        ]