from django.test import TestCase
from tests.utils import (
    create_and_validate_custom_notification,
    create_and_validate_custom_user
)
from django.db.utils import IntegrityError


class NotificationTest(TestCase):

    def test_given_right_notification_when_signup_then_returns_right_info(self):
        user = create_and_validate_custom_user(email='right_notification@test.test')
        notification = create_and_validate_custom_notification(user=user)

        self.assertEqual(notification.notification, 'signup')
        self.assertEqual(notification.user.email, 'right_notification@test.test')

    def test_given_notification_not_provided_when_creating_then_validation_error(self):
        with self.assertRaises(IntegrityError):
            user = create_and_validate_custom_user(email='notification_none@test.test')
            create_and_validate_custom_notification(user=user, notification=None)
