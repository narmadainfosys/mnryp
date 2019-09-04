from django.test import TestCase
from datetime import datetime
from categories.models import Category,Listing
from categories.views import categories,category,listings,listing
from django.urls import reverse
# Create your tests here.

class CategoriesTest(TestCase):
    def setUp(self):
        self.c = Category.objects.create(name='Test category 1',summary='This is test category 1')

    def test_category_creation(self):

        self.assertEqual(self.c.name,'Test category 1')
        self.assertEqual(self.c.summary, 'This is test category 1')
        self.assertEqual(self.c.slug, 'test-category-1')
        self.assertEqual(self.c.__str__(), self.c.name)
        self.assertTrue(isinstance(self.c, Category))

    def test_category_list_view(self):
        url = reverse('categories')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.c.name.encode(), resp.content)

    def test_category_detail_view(self):
        url = reverse('category', args=[self.c.slug])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.c.name.encode(), resp.content)

class ListingsTest(TestCase):
    post_data = {
            'category': '4',
            'title': 'Test listing',
            'short_description': 'Short desc',
            'full_description': 'Full desc',
            'contact_person': 'Test person',
            'business_address': 'Test business address',
            'email_address': 'test@gmail.com',
            'phone_number': '9801234567',
            'zip_code': '10400'
            }

    def setUp(self):
        self.c = Category.objects.create(name='Test category 1',summary='This is test category 1')
        self.l = Listing.objects.create(category=self.c,
                title='Test listing',
                short_description='Short desc',
                full_description='Full desc',
                contact_person='Test person',
                business_address='Test business address',
                phone_number='9812111122',
                zip_code='10400',)
    def test_listing_creation(self):
        self.assertEqual(self.l.category, self.c)
        self.assertEqual(self.l.title, 'Test listing')
        self.assertEqual(self.l.short_description, 'Short desc')
        self.assertEqual(self.l.full_description, 'Full desc')
        self.assertEqual(self.l.contact_person, 'Test person')
        self.assertEqual(self.l.business_address, 'Test business address')
        self.assertEqual(self.l.phone_number, '9812111122')
        self.assertEqual(self.l.zip_code, '10400')
        self.assertEqual(self.l.slug, 'test-listing')
        self.assertEqual(self.l.__str__(), self.l.title)
        self.assertTrue(isinstance(self.l, Listing))

    def test_listing_list_view(self):
        url = reverse('listings')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.l.title.encode(), resp.content)

    def test_listing_detail_view(self):
        url = reverse('listing', args=[self.l.slug])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.l.title.encode(), resp.content)

    def test_create_listing_view(self):
        url = reverse('create_listing')
        resp = self.client.get(url)
        resp_post = self.client.post(url, data=self.post_data, follow=True)
        expected_url = reverse('listings')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'categories/create_listing.html')

        self.assertEqual(resp_post.status_code, 200)
        self.assertRedirects(resp_post, expected_url, status_code=302,
                            target_status_code=200)

    def test_edit_listing_view(self):
        url = reverse('edit_listing', args = [self.l.slug])
        resp = self.client.get(url)
        form = resp.context['form']
        data = form.initial
        expected_url = reverse('listings')

        data['title'] = 'edited title'

        resp_post = self.client.post(url, data=data, follow=True)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'categories/edit_listing.html')

        self.assertEqual(resp_post.status_code, 200)
        self.assertRedirects(resp_post, expected_url, status_code=302,
                            target_status_code=200)
        self.assertEqual(resp.context['form'].initial['title'], 'edited title')

    def test_delete_listing_view(self):
        slug = self.l.slug
        url = reverse('delete_listing', args = [slug])
        resp = self.client.get(url)
        listing = resp.context['listing']
        expected_url = reverse('listings')

        resp_post = self.client.post(url, follow=True)

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'categories/delete_listing.html')

        resp = self.client.get(url, args = [slug], follow=True)

        self.assertEqual(resp_post.status_code, 200)
        self.assertRedirects(resp_post, expected_url, status_code=302,
                            target_status_code=200)
        self.assertEqual(resp.status_code ,404)

    def test_search_view(self):
        url = reverse('search')
        data = {'q':'Test Listing'}
        resp = self.client.get(url, data=data)

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'categories/listings.html')

        self.assertTrue(self.l in resp.context['items'])

