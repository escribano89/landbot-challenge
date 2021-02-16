from celery import shared_task
from landbot.notifications.context import NotificationContext
from landbot.models import Notification


@shared_task
def send_notification(notification_id):
    """
    Uses de context to build the strategy and send the notification
    """
    notification = Notification.objects.get(id=notification_id)
    # Use the context to setup the strategy
    # and then send the notification
    context = NotificationContext(notification.user, notification.notification)
    context.strategy.send()
    # Update the sent flag
    Notification.objects.filter(id=notification_id).update(sent=True)
