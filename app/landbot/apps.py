from django.apps import AppConfig
from django.db.models.signals import post_save


class LandbotConfig(AppConfig):
    name = 'landbot'

    def ready(self):
        # Registering signals with the model's string label
        from landbot.signals.signup import save_user
        from landbot.signals.notification_created import save_notification
        post_save.connect(save_user, sender='landbot.ExtendedUser', dispatch_uid="send_user_created")
        post_save.connect(save_notification, sender='landbot.Notification', dispatch_uid="send_notification")
