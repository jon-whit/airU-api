from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTestCase(TestCase):

    def test_user_created(self):
        """
        Test to verify user creation.

        Verify the User object is retrievable after creation and that the
        username matches the one specified during object creation. 
        """
        username = 'test-user'
        User.objects.create(username=username)
        user = User.objects.get(username=username)
        self.assertEqual(user.username, username)

    def test_user_delete(self):
        """
        Test to verify user deletion.

        Verify a single User object is created and that the number of User objects
        is equal to 0 after deletion.
        """
        username = 'test-user'
        User.objects.create(username=username)
        self.assertEqual(User.objects.count(), 1)
        User.objects.get(username=username).delete()
        self.assertEqual(User.objects.count(), 0)
