from django.contrib.auth.models import User
from django.test import TestCase

class UserTest(TestCase):

    def test_create_user(self):
        """Test creating a new user (in order to setup the environment)"""

        username = None
        email = 'test@test.test'

        user = User.objects.create(
            username=username,
            email=email,
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
