from landbot.notifications.mapping import TOPIC_CHANNELS_MAPPING


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
        self.strategy = TOPIC_CHANNELS_MAPPING[notification](user)

    def send(self):
        self.strategy.send()
