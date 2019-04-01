from django.test import TestCase
from datetime import datetime
from categories.models import Category
# Create your tests here.

class CategoriesTest(TestCase):
    def create_category(self, name='Test category 1',summary='This is test category 1'):
        return Category.objects.create(name=name,summary=summary)

    def test_category_creation(self):
        c = self.create_category()

        self.assertEqual(c.name,'Test category 1')
        self.assertEqual(c.summary, 'This is test category 1')
        self.assertEqual(c.slug, 'test-category-1')
        self.assertEqual(c.__str__(), c.name)
        self.assertTrue(isinstance(c, Category))
