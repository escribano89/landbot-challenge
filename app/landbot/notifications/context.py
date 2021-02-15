from importlib import import_module

STRATEGIES_MODULE = 'landbot.notifications.strategies'


class NotificationContext():
    """
    The Context defines the interface of interest to clients
    who need to use notifications
    """
    def __init__(self, strategy: str, notification: str) -> None:
        """
        The Context accepts the strategy and the notification
        in order to setup the concrete notification
        """
        # We look for the available strategies for the
        # provided notification
        strategies_available = import_module('landbot.notifications.{}'.format(notification.lower()))
        strategies_dict = getattr(strategies_available, 'STRATEGIES')

        # We get the selected strategy class
        module = import_module('{}.{}'.format(STRATEGIES_MODULE, strategy))
        strategy_ = getattr(module, strategy.capitalize())

        self.strategy = strategy_(strategies_dict.get(strategy))

    def send(self, to) -> None:
        self.strategy.send(to)
