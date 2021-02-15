from django.test import TestCase
from rest_framework import status
from landbot.models import Notification
from django.test.utils import override_settings
from landbot.tasks.signup import signup_notification
from unittest.mock import patch
from tests.utils import create_and_validate_custom_user
from django.core import mail
from landbot.notifications.signup import STRATEGIES

class SignupTask(TestCase):

    @override_settings(CELERY_TASK_EAGER_PROPAGATES=True,
                       CELERY_TASK_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')

    def test_given_signup_task_when_called_then_notification_and_email_triggered(self):
        user = create_and_validate_custom_user(email='signup@test.test')

        signup_notification(strategy='email', notification='signup', user=user)

        # Assert that notification db row has been updated properly
        notification = Notification.objects.get(user=user)
        self.assertEquals(notification.sent, True)
        # Now we can test delivery and email contents
        assert len(mail.outbox) == 1, "Inbox is not empty"
        assert mail.outbox[0].subject == STRATEGIES.get('email').get('subject')
        assert mail.outbox[0].body == STRATEGIES.get('email').get('body')
        assert mail.outbox[0].from_email == STRATEGIES.get('email').get('from')
        assert mail.outbox[0].to == [user.email]
