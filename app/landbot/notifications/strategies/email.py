from django.core.mail import send_mail
from landbot.notifications.strategies.strategy import NotificationStrategy


class Email(NotificationStrategy):

    def __init__(self, params):
        self.params = params

    def send(self, to: str) -> None:
        """Sends the email using the django core"""

        send_mail(
            self.params.get('subject'),
            self.params.get('body'),
            self.params.get('from'),
            [to],
        )
