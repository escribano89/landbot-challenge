from django.test import TestCase
from tests.utils import (
    create_and_validate_custom_user,
    create_and_validate_custom_notification
)
from django.db.utils import IntegrityError


class NotificationTest(TestCase):

    def test_given_right_notification_when_create_then_returns_right_info(self):
        strategy = 'email'
        user = create_and_validate_custom_user()
        notification = create_and_validate_custom_notification(user=user)

        self.assertEqual(notification.notification, 'welcome_message')
        self.assertEqual(notification.strategy, strategy)
        self.assertEqual(notification.user.email, user.email)

    def test_given_notification_not_provided_when_creating_then_validation_error(self):
        with self.assertRaises(IntegrityError):
            user = create_and_validate_custom_user(email='without_notification@test.test')
            create_and_validate_custom_notification(user=user, notification=None)

    def test_given_strategy_not_provided_when_creating_then_validation_error(self):
        with self.assertRaises(IntegrityError):
            user = create_and_validate_custom_user(email='without_strategy@test.test')
            create_and_validate_custom_notification(user=user, strategy=None)

    def test_given_user_not_provided_when_creating_then_validation_error(self):
        with self.assertRaises(IntegrityError):
            create_and_validate_custom_notification(user=None)
