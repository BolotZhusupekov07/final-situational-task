from django.urls import include, path
from rest_framework.routers import DefaultRouter

from product import views
from product.category.urls import router as category_router

router = DefaultRouter()
router.register(r"api/products", views.ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(category_router.urls)),
]
