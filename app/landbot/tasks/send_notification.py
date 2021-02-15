from celery import shared_task
from landbot.notifications.context import NotificationContext
from landbot.models import Notification


@shared_task
def send_notification(notification_id):
    notification = Notification.objects.get(id=notification_id)
    # Use the context to setup the strategy
    # and then send the email
    context = NotificationContext(notification.strategy, notification.notification)
    context.strategy.send(notification.customer_email)
    # Update the sent flag
    Notification.objects.filter(id=notification_id).update(sent=True)