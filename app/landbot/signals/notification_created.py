from landbot.tasks.send_notification import send_notification


def save_notification(sender, instance, **kwargs):
    send_notification(instance.id)
