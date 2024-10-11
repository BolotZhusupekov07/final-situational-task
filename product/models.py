from django.db import models

from product.category.models import ProductCategory


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    category = models.ForeignKey(ProductCategory, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
