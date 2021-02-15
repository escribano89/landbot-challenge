from landbot.tasks.signup import signup_notification


def save_user(sender, instance, **kwargs):
    signup_notification(strategy='email', notification='signup', user=instance)