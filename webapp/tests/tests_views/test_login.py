from django.test import TestCase


class TestGetLoginView(TestCase):
    URL = '/carnival/login'

    def setUp(self):
        self.response = self.client.get(self.URL, follow=True)

    def test_renders_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'login.html')

    def test_sensitive_post_parameters(self):
        self.assertEqual(self.response.context.request.sensitive_post_parameters, ('password', ))

    def test_never_cache_headers(self):
        self.assertEqual(self.response['Cache-Control'], 'max-age=0, no-cache, no-store, must-revalidate')
