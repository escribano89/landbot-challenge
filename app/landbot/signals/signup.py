from landbot.models import Notification


def save_user(sender, instance, **kwargs):
    """
    Process the sign up notification
    """
    # Create the notification in order to trigger the related signal
    Notification.objects.create(
        notification='signup',
        user=instance
    )
