from django.conf import settings
from landbot.notifications.strategies.email import send_email_wrapper


class Pricing():
    def __init__(self, user):
        """
            Pricing notification using email. Includes
            the user who requested assistance
        """
        # User is mandatory for the pricing notification
        if not user:
            raise(Exception)

        self.user = user
        self.subject = 'Requested pricing assistance'
        self.body = 'The user {} has requested pricing assistance'.format(user.email)
        self.source = settings.EMAIL_FROM
        self.to = settings.EMAIL_PRICING

    def send(self):
        # Wrapper in order to ease interchangibility
        send_email_wrapper(self.subject, self.body, self.source, self.to)
