from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class StaticPagesTest(TestCase):

    def test_template_used(self):
        url_about = reverse('about')
        url_home = reverse('home')
        url_contact = reverse('contact')
        url_privacy = reverse('privacy_policy')

        resp_about = self.client.get(url_about)
        resp_home = self.client.get(url_home)
        resp_contact = self.client.get(url_contact)
        resp_privacy = self.client.get(url_privacy)

        self.assertTemplateUsed(resp_about, 'static_pages/about.html')
        self.assertTemplateUsed(resp_home, 'static_pages/home.html')
        self.assertTemplateUsed(resp_contact, 'static_pages/contact.html')
        self.assertTemplateUsed(resp_privacy, 'static_pages/privacy_policy.html')
