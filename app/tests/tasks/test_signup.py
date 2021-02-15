from django.test import TestCase
from landbot.models import Notification, ExtendedUser
from django.test.utils import override_settings
from django.core import mail
from landbot.notifications.signup import STRATEGIES


class SignupTask(TestCase):

    @override_settings(CELERY_TASK_EAGER_PROPAGATES=True,
                       CELERY_TASK_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_given_signup_task_when_called_then_notification_is_created_and_processed(self):
        # Clean up the notifications table
        Notification.objects.all().delete()

        user = ExtendedUser.objects.create(
            email='test-signup@test.test',
            first_name='Javier',
            phone='+41524204242',
            origin='landbot',
        )

        user.set_unusable_password()
        user.clean_fields()

        # Assert that notification db row has been updated properly
        notification = Notification.objects.get(customer_email=user.email)
        self.assertEquals(notification.sent, True)

        # Now we can test delivery and email contents
        assert len(mail.outbox) == 1, "Inbox is not empty"
        assert mail.outbox[0].subject == STRATEGIES.get('email').get('subject')
        assert mail.outbox[0].body == STRATEGIES.get('email').get('body')
        assert mail.outbox[0].from_email == STRATEGIES.get('email').get('from')
        assert mail.outbox[0].to == [user.email]
