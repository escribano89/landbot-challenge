from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from landbot.models import Notification
from django.urls import reverse
from django.test.utils import override_settings
from tests.utils import create_and_validate_custom_user

ASSISTANCE_URL = reverse('user-assistance')


class ApiAssistanceTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def send_post(self, url, topic, email):
        return self.client.post(
            url,
            {
                'topic': topic,
                'email': email,

            },
        )

    @override_settings(CELERY_TASK_EAGER_PROPAGATES=True,
                       CELERY_TASK_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_given_assistance_request_when_email_and_topic_sales_are_correct_then_ok_response(self):
        # Clean up the notifications table
        Notification.objects.all().delete()

        user = create_and_validate_custom_user(email='assistance-sales@test.test')
        res = self.send_post(ASSISTANCE_URL, email='assistance-sales@test.test', topic='sales')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # Assert that notification db row has been updated properly
        notification = Notification.objects.get(id=user.id)
        self.assertEquals(notification.sent, True)

    @override_settings(CELERY_TASK_EAGER_PROPAGATES=True,
                       CELERY_TASK_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_given_assistance_request_when_email_and_topic_pricing_are_correct_then_ok_response(self):
        # Clean up the notifications table
        Notification.objects.all().delete()

        user = create_and_validate_custom_user(email='assistancepricing@test.test')
        res = self.send_post(ASSISTANCE_URL, email='assistancepricing@test.test', topic='pricing')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # Assert that notification db row has been updated properly
        notification = Notification.objects.get(id=user.id)
        self.assertEquals(notification.sent, True)

    def test_given_assistance_request_when_invalid_topic_then_bad_request(self):
        create_and_validate_custom_user(email='invalidtopic@test.test')
        res = self.send_post(ASSISTANCE_URL, email='invalidtopic@test.test', topic='fake')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_assistance_request_when_invalid_email_then_bad_request(self):
        res = self.send_post(ASSISTANCE_URL, email='inventedemail@test.com', topic='sales')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_assistance_request_when_empty_topic_then_bad_request(self):
        create_and_validate_custom_user(email='emptytopic@test.test')
        res = self.send_post(ASSISTANCE_URL, email='emptytopic@test.test', topic='')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_given_assistance_request_when_empty_email_then_bad_request(self):
        res = self.send_post(ASSISTANCE_URL, email='', topic='sales')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
