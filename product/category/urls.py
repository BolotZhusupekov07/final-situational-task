from django.urls import include, path
from rest_framework.routers import DefaultRouter

from product.category import views

router = DefaultRouter()
router.register(
    r"api/product-categories",
    views.ProductCategoryViewSet,
    basename="product-categories",
)

urlpatterns = [path("", include(router.urls))]
