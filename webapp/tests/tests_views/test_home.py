from django.test import TestCase


class TestHomeView(TestCase):
    URL = '/carnival/home'

    def test_renders_template_without_login(self):
        response = self.client.get(self.URL, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')