from django.test import TestCase


class TestHomeView(TestCase):
    URL = '/carnival'

    def test_renders_template_without_login(self):
        response = self.client.get(self.URL, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_renders_template_login(self):
        response = self.client.get(self.URL, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
