from landbot.models import Notification


def signup_notification(user, notification):
    # Create the notification in order to trigger the related signal
    Notification.objects.create(
        notification=notification,
        user=user
    )
