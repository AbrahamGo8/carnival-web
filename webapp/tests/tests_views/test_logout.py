from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase


class LogoutViewTestCase(TestCase):
    URL = '/carnival/logout'

    def test_renders_template(self):
        response = self.client.get(self.URL, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_logout(self):
        user = User.objects.create_user('sonar', password='sonar2017')
        data = {
            'username': user.username,
            'password': 'sonar2017'
        }

        response_login = self.client.post('/carnival/login', data=data, follow=True)

        self.assertTrue(response_login.context.request.user.password)
        self.assertTrue(response_login.context.request.user.username)

        response_logout = self.client.get(self.URL, follow=True)

        self.assertIsInstance(response_logout.context['request'].user, AnonymousUser)
        self.assertFalse(response_logout.context['request'].user.username)
