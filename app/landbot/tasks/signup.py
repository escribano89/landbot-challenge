from landbot.models import Notification


def signup_notification(strategy, notification, customer_email):
    # Create the notification in order to trigger the related signal
    Notification.objects.create(
        strategy=strategy,
        notification=notification,
        customer_email=customer_email
    )
