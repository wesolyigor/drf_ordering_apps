from django.test import TestCase

from api.models import Category, Offer
from api.serializers import CategorySerializer, OfferSerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category_test = Category.objects.get_or_create(
            name="test"
        )[0]
        self.serializer_category = CategorySerializer(instance=self.category_test)
        self.category_attributes = {
            "name": "category_test",
            "ordering": 1
        }

    def test_model_fields(self):
        data = self.serializer_category.data
        self.assertEqual(data.keys(), {"id", "name", "ordering"})

    def test_default_value_ordering_field(self):
        data = self.serializer_category.data
        self.assertEqual(data["ordering"], 0)

    def test_field_content(self):
        data = self.category_attributes
        self.assertEqual(data["name"], self.category_attributes['name'])
        self.assertEqual(data["ordering"], self.category_attributes['ordering'])


class TestOfferSerializer(TestCase):
    def setUp(self) -> None:
        self.category_test = Category.objects.get_or_create(
            name="test"
        )[0]
        self.offer_test = Offer.objects.get_or_create(
            title="pizza",
            category=self.category_test,
            description="Fantastic dish, recommend for all family.",
            price=12.50
        )[0]
        self.serializer_offer = OfferSerializer(instance=self.offer_test)
        self.offer_attributes = {
            "name": "pizza",
        }

    def test_model_fields(self):
        data = self.serializer_offer.data
        self.assertEqual(data.keys(), {"id", "title", "category", "description", "price", "created_at"})

