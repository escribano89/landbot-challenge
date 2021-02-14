from django.test import TestCase
from landbot.notifications.context import NotificationContext
from landbot.notifications.strategies.email import Email
from landbot.notifications.signup import STRATEGIES
from unittest import mock


class ContextTest(TestCase):

    def test_given_context_when_email_strategy_then_setup_correctly(self):
        strategy = 'email'
        email_strategy = Email(STRATEGIES.get(strategy))

        context = NotificationContext(strategy=strategy, notification='signup')
        self.assertEqual(context.strategy.params, email_strategy.params)

    def test_given_strategy_send_method_when_is_called_then_calls_strategy(self):
        strategy = 'email'
        email_strategy = Email(STRATEGIES.get(strategy))

        context = NotificationContext(strategy=strategy, notification='signup')
        self.assertEqual(context.strategy.params, email_strategy.params)

        with mock.patch('landbot.notifications.strategies.email.Email.send', return_value=True) as mocked_handler:
            context.strategy.send('javier@test.test')
            self.assertEquals(mocked_handler.call_count, 1)

    def test_given_context_with_unknown_strategy_then_setup_fails(self):
        with self.assertRaises(Exception):
            strategy = 'whatsapp'
            email_strategy = Email(STRATEGIES.get(strategy))

            context = NotificationContext(strategy=strategy, notification='signup')
            self.assertEqual(context.strategy.params, email_strategy.params)

    def test_given_context_with_unknown_notification_then_setup_fails(self):
        with self.assertRaises(Exception):
            strategy = 'whatsapp'
            email_strategy = Email(STRATEGIES.get(strategy))

            context = NotificationContext(strategy=strategy, notification='signup_fake')
            self.assertEqual(context.strategy.params, email_strategy.params)
