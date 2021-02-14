from django.core.mail import send_mail
from landbot.notifications.strategies.strategy import NotificationStrategy


class Email(NotificationStrategy):

    def __init__(self, params):
        self.params = params

    def send(self, user_unique_key: str) -> None:
        """Sends the email using the django core"""

        send_mail(
            self.params.get('subject'),
            self.params.get('body'),
            self.params.get('from'),
            [user_unique_key],
        )
