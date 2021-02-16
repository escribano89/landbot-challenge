from django.conf import settings
from landbot.notifications.strategies.email import send_email_wrapper


class Sales():
    #TODO Add slack message not email
    def __init__(self, user):
        # User is mandatory for the sign up notification
        if not user:
            raise(Exception)

        self.user = user
        self.subject = 'Requested sales assistance'
        self.body = 'The user {} has requested sales assistance'.format(user.email)
        self.source = settings.EMAIL_FROM
        self.to = settings.EMAIL_SALES

    def send(self):
        # Wrapper in order to ease interchangibility
        send_email_wrapper(self.subject, self.body, self.source, self.to)