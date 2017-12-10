from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User

class UserViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser_name = 'admin-user'
        self.superuser_pass = 'secret'
        self.superuser_email = 'admin-user@example.com'
        self.superuser = User.objects.create_superuser(username=self.superuser_name, password=self.superuser_pass, email=self.superuser_email) 
 
    def test_list_users_anony_user(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_users_auth_user(self):
        self.client.login(username=self.superuser_name, password=self.superuser_pass)
        response = self.client.get('/users/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
