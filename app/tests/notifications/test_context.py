from django.test import TestCase
from landbot.notifications.context import NotificationContext
from landbot.notifications.signup import Signup
from landbot.notifications.sales import Sales
from landbot.notifications.pricing import Pricing
from unittest import mock
from tests.utils import create_and_validate_custom_user
from django.conf import settings


class ContextTest(TestCase):
    def test_given_signup_context_when_right_params_then_setup_correctly(self):
        user = create_and_validate_custom_user(email='right@test.test')
        context = NotificationContext(user=user, notification='signup')
        self.assertTrue(isinstance(context.strategy, Signup))
        self.assertEqual(context.strategy.to, 'right@test.test')

    def test_given_pricing_when_right_params_then_setup_correctly(self):
        user = create_and_validate_custom_user(email='pricing@test.test')
        context = NotificationContext(user=user, notification='pricing')
        self.assertTrue(isinstance(context.strategy, Pricing))
        self.assertEqual(context.strategy.source, settings.EMAIL_FROM)
        self.assertEqual(context.strategy.to, settings.EMAIL_PRICING)

    def test_given_sales_when_right_params_then_setup_correctly(self):
        user = create_and_validate_custom_user(email='sales@test.test')
        context = NotificationContext(user=user, notification='sales')
        self.assertTrue(isinstance(context.strategy, Sales))

    def test_given_signup_context_when_sending_then_calls_strategy(self):
        user = create_and_validate_custom_user(email='sending@test.test')
        context = NotificationContext(user=user, notification='signup')

        with mock.patch('landbot.notifications.signup.Signup.send', return_value=True) as mocked_handler:
            context.strategy.send()
            self.assertEquals(mocked_handler.call_count, 1)

    def test_given_pricing_context_when_sending_then_calls_strategy(self):
        user = create_and_validate_custom_user(email='sendingpricing@test.test')
        context = NotificationContext(user=user, notification='pricing')

        with mock.patch('landbot.notifications.pricing.Pricing.send', return_value=True) as mocked_handler:
            context.strategy.send()
            self.assertEquals(mocked_handler.call_count, 1)

    def test_given_sales_context_when_sending_then_calls_strategy(self):
        user = create_and_validate_custom_user(email='sendingsales@test.test')
        context = NotificationContext(user=user, notification='sales')

        with mock.patch('landbot.notifications.sales.Sales.send', return_value=True) as mocked_handler:
            context.strategy.send()
            self.assertEquals(mocked_handler.call_count, 1)

    def test_given_context_with_unknown_notification_then_setup_fails(self):
        with self.assertRaises(Exception):
            user = create_and_validate_custom_user(email='fake-notification@test.test')
            NotificationContext(user=user, notification='whatsapp-fake')

    def test_given_context_with_signuo_notification_and_no_user_then_setup_fails(self):
        with self.assertRaises(Exception):
            NotificationContext(user=None, notification='whatsapp-fake')
