from importlib import import_module


class NotificationContext():
    """
    The Context defines the interface of interest to clients
    who need to use notifications
    """
    def __init__(self, user, notification):
        """
        The Context accepts the notification
        in order to setup the concrete notification
        """
        # We import the provided notification
        notification_module = import_module('landbot.notifications.{}'.format(notification.lower()))
        strategy_ = getattr(notification_module, notification.capitalize())
        self.strategy = strategy_(user)

    def send(self):
        self.strategy.send()
