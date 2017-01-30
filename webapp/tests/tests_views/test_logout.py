from django.test import TestCase


class TestGetLoginView(TestCase):
    URL = '/carnival/logout'

    def setUp(self):
        self.response = self.client.get(self.URL, follow=True)

    def test_renders_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'login.html')
