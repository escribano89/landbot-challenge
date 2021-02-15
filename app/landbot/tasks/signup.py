from celery import shared_task
from django.core.mail import send_mail
from landbot.notifications.context import NotificationContext
from landbot.models import Notification


def signup_notification(strategy, notification, user):
    # Create the notification row to check if it has been sent afterwards
    Notification.objects.create(
        strategy=strategy,
        notification=notification,
        user=user
    )
    # Delay the task
    send.delay(strategy, notification, user.email)

@shared_task
def send(strategy, notification, to):
    # Use the context to setup the strategy
    # and then send the email
    context = NotificationContext(strategy, notification)
    context.strategy.send(to)
