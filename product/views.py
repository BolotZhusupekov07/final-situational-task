import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from product.models import Product
from product.serializers import (
    ProductCreateUpdateSerializer,
    ProductSerializer,
)


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title", lookup_expr="icontains"
    )
    category = django_filters.CharFilter(
        label="category", field_name="category__title", lookup_expr="icontains"
    )

    class Meta:
        model = Product
        fields = ["title", "category"]


class ProductViewSet(viewsets.ModelViewSet):
    model = Product
    queryset = Product.objects.all().order_by("-title")
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ["price"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ProductCreateUpdateSerializer
        elif self.action in ["retrieve", "list"]:
            return ProductSerializer
        return super().get_serializer_class()
