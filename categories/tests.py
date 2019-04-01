from django.test import TestCase
from datetime import datetime
from categories.models import Category
from categories.views import categories,category
from django.urls import reverse
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

    def test_category_list_view(self):
        c = self.create_category()
        url = reverse('categories')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(c.name.encode(), resp.content)

    def test_category_detail_view(self):
        c = self.create_category()
        url = reverse('category', args=[c.slug])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(c.name.encode(), resp.content)
