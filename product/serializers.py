from rest_framework import serializers

from product.category.serializers import ProductCategorySerializer
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "category",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class ProductCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "category",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
