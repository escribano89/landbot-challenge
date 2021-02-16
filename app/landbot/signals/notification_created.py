from landbot.tasks.send_notification import send_notification


def save_notification(sender, instance, **kwargs):
    """
    Sends the notification using the model reference
    """
    send_notification(instance.id)
