from django.test import TestCase
from landbot.models import Notification
from django.test.utils import override_settings
from django.core import mail
from tests.utils import create_and_validate_custom_user


class SendNotificationTaskTest(TestCase):

    @override_settings(CELERY_TASK_EAGER_PROPAGATES=True,
                       CELERY_TASK_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_given_signup_notification_when_created_then_is_processed(self):
        # Clean up the notifications table
        Notification.objects.all().delete()

        user = create_and_validate_custom_user(email='test_send_not@test.test')
        notification = Notification.objects.create(
            notification='signup',
            user=user,
        )
        # Assert that notification db row has been updated properly
        notification = Notification.objects.get(id=notification.id)
        self.assertEquals(notification.sent, True)

        # Now we can test delivery and email contents
        assert len(mail.outbox) == 1, "Inbox is not empty"
        assert mail.outbox[0].to == [user.email]
