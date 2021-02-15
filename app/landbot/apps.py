from django.apps import AppConfig
from django.db.models.signals import post_save


class LandbotConfig(AppConfig):
    name = 'landbot'

    def ready(self):
        # Registering signals with the model's string label
        from landbot.signals.signup import save_user
        post_save.connect(save_user, sender='landbot.ExtendedUser', dispatch_uid="send_welcome_msg")
