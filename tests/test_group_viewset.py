from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import Group, User

class GroupViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser_name = 'admin-user'
        self.superuser_pass = 'secret'
        self.superuser_email = 'admin-secret@example.com'
        self.superuser = User.objects.create_superuser(username=self.superuser_name,
					password=self.superuser_pass, email=self.superuser_email)

    def test_create_group_anony_user(self):
        """
        Test Group creation with anonymous user.

        This tests the POST endpoint for the Group view under an
        anonymous user.
        """
        response = self.client.post('/groups/', {'name': 'new-group'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Group.objects.count(), 0)

    def test_create_group_admin_user(self):
        """
        Test Group creation with superuser.

        This tests the POST endpoint for the Group view under superuser
        authentication.
        """
        self.client.login(username=self.superuser_name, password=self.superuser_pass)

        response = self.client.post('/groups/', {'name': 'new-group'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(Group.objects.get().name, 'new-group')

        self.client.logout()

    def test_list_groups_anony_user(self):
        response = self.client.get('/groups/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_groups_admin_user(self):
        self.client.login(username=self.superuser_name, password=self.superuser_pass)

        response = self.client.get('/groups/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.logout()
