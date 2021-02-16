from landbot.tasks.signup import signup_notification


def save_user(sender, instance, **kwargs):
    signup_notification(notification='signup', user=instance)
