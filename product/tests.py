from rest_framework import status
from rest_framework.test import APITestCase

from product.category.models import ProductCategory
from product.models import Product


class ProductAPITests(APITestCase):
    def setUp(self):
        self.product_category = ProductCategory.objects.create(title="title")
        self.product = Product.objects.create(
            title="product title",
            description="product description",
            category=self.product_category,
            price=100,
        )

    def test_get_products(self):
        response = self.client.get("/api/products/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_products(self):
        response = self.client.post(
            "/api/products/",
            data={
                "title": "title",
                "description": "description",
                "category": self.product_category.id,
                "price": 100,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["title"], "title")
        self.assertEqual(response.json()["description"], "description")
        self.assertEqual(response.json()["category"], self.product_category.id)
        self.assertEqual(response.json()["price"], "100.00")

    def test_update_products(self):
        response = self.client.patch(
            f"/api/products/{self.product.id}/",
            data={
                "title": "new title",
            },
            params={"id": self.product.id},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()["title"], "new title")

    def test_delete_products(self):
        response = self.client.delete(
            f"/api/products/{self.product.id}/", params={"id": self.product.id}
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
