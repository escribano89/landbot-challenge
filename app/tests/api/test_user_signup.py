from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from landbot.models import ExtendedUser, Notification
from django.urls import reverse
from django.test.utils import override_settings

SIGNUP_URL = reverse('create-user')


class ApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def send_post(self, url, first_name='Javier', email='test@test.test', phone='+41524204242', origin='landbot'):
        return self.client.post(
            url,
            {
                'first_name': first_name,
                'email': email,
                'phone': phone,
                'origin': origin,
            },
        )

    @override_settings(CELERY_TASK_EAGER_PROPAGATES=True,
                       CELERY_TASK_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_given_user_when_signup_post_then_created_ok(self):
        res = self.send_post(SIGNUP_URL)
        user = ExtendedUser.objects.get(email='test@test.test')

        self.assertTrue(isinstance(user, ExtendedUser))
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # Assert that notification db row has been updated properly
        notification = Notification.objects.get(user=user)
        self.assertEquals(notification.sent, True)

    def test_given_user_when_signup_with_wrong_email_then_bad_request(self):
        res = self.send_post(SIGNUP_URL, email='42')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_user_when_signup_with_wrong_phone_then_bad_request(self):
        res = self.send_post(SIGNUP_URL, phone='42')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_user_when_signup_with_empty_first_name_then_bad_request(self):
        res = self.send_post(SIGNUP_URL, first_name='')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_user_when_signup_with_empty_email_then_bad_request(self):
        res = self.send_post(SIGNUP_URL, email='')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_user_when_signup_with_empty_origin_then_bad_request(self):
        res = self.send_post(SIGNUP_URL, origin='')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_user_when_signup_with_empty_phone_then_bad_request(self):
        res = self.send_post(SIGNUP_URL, phone='')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_user_when_signup_post_without_first_name_then_bad_request(self):

        email = 'test@test.test'
        phone = '+41524204242'
        origin = 'landbot'

        res = self.client.post(
            SIGNUP_URL,
            {
                'email': email,
                'phone': phone,
                'origin': origin,
            },
        )

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_user_when_signup_post_without_origin_then_bad_request(self):
        first_name = 'Javier'
        email = 'test@test.test'
        phone = '+41524204242'

        res = self.client.post(
            SIGNUP_URL,
            {
                'email': email,
                'phone': phone,
                'first_name': first_name,
            },
        )

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_user_when_signup_post_without_phone_then_bad_request(self):
        first_name = 'Javier'
        email = 'test@test.test'
        origin = 'landbot'

        res = self.client.post(
            SIGNUP_URL,
            {
                'email': email,
                'first_name': first_name,
                'origin': origin
            },
        )

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_user_when_signup_post_without_email_then_bad_request(self):
        first_name = 'Javier'
        phone = '+41524204242'
        origin = 'landbot'

        res = self.client.post(
            SIGNUP_URL,
            {
                'phone': phone,
                'first_name': first_name,
                'origin': origin
            },
        )

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    @override_settings(CELERY_TASK_EAGER_PROPAGATES=True,
                       CELERY_TASK_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_given_user_when_signup_twice_then_ok_and_bad(self):
        first_name = 'Javier'
        phone = '+41524204242'
        origin = 'landbot'
        email = 'test_twice@test.test'

        res = self.client.post(
            SIGNUP_URL,
            {
                'phone': phone,
                'first_name': first_name,
                'origin': origin,
                'email': email
            },
        )

        user = ExtendedUser.objects.get(email=email)
        self.assertTrue(isinstance(user, ExtendedUser))
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        res = self.client.post(
            SIGNUP_URL,
            {
                'phone': phone,
                'first_name': first_name,
                'origin': origin,
                'email': email
            },
        )

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
