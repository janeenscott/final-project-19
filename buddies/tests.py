from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):

    def test_index(self):
        view_url = reverse('buddies:index')
        response = self.client.get(view_url)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        view_url = reverse('login')
        response = self.client.get(view_url)
        self.assertEqual(response.status_code, 200)
