from rest_framework import serializers

from product.category.models import ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            "id",
            "title",
        ]
        read_only_fields = ["id"]
