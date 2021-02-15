from django.test import TestCase
from tests.utils import create_and_validate_custom_notification
from django.db.utils import IntegrityError


class NotificationTest(TestCase):

    def test_given_right_notification_when_signup_then_returns_right_info(self):
        strategy = 'email'
        notification = create_and_validate_custom_notification(customer_email='customer@test.test')

        self.assertEqual(notification.notification, 'signup')
        self.assertEqual(notification.strategy, strategy)
        self.assertEqual(notification.customer_email, 'customer@test.test')

    def test_given_notification_not_provided_when_creating_then_validation_error(self):
        with self.assertRaises(IntegrityError):
            create_and_validate_custom_notification(customer_email='customer@test.test', notification=None)

    def test_given_strategy_not_provided_when_creating_then_validation_error(self):
        with self.assertRaises(IntegrityError):
            create_and_validate_custom_notification(customer_email='customer@test.test', strategy=None)

    def test_given_customer_email_not_provided_when_creating_then_validation_error(self):
        with self.assertRaises(IntegrityError):
            create_and_validate_custom_notification(customer_email=None)
