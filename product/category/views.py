from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from product.category.models import ProductCategory
from product.category.serializers import ProductCategorySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    model = ProductCategory
    queryset = ProductCategory.objects.all().order_by("-title")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title"]
