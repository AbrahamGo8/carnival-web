from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.test import TestCase


class LoginViewTestCase(TestCase):
    URL = '/carnival/login'

    def test_renders_template(self):
        response = self.client.get(self.URL, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_passes_form(self):
        response = self.client.get(self.URL)

        self.assertIsInstance(response.context['form'], AuthenticationForm)

    def test_POST_redirect(self):
        user = User.objects.create_user('sonar', password='sonar2017')
        data = {
            'username': user.username,
            'password': 'sonar2017'
        }
        response = self.client.post(self.URL, data=data, follow=True)

        self.assertTrue(response.context.request.user.password)
        self.assertTrue(response.context.request.user.username)
        self.assertTemplateUsed(response, 'home.html')
