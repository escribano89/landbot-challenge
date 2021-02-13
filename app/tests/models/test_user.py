from django.contrib.auth.models import User
from django.test import TestCase


class UserTest(TestCase):

    def test_given_extended_user_when_create_then_returns_user(self):
        username = 'test'
        email = 'test@test.test'

        user = User.objects.create(
            username=username,
            email=email,
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
