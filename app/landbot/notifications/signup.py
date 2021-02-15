from django.conf import settings
from landbot.notifications.strategies.email import send_email_wrapper

class Signup():
    def __init__(self, user):
        # User is mandatory for the sign up notification
        if not user:
            raise(Exception)

        self.user = user
        self.subject = 'Welcome to landbot!'
        self.body = 'The entire team is thrilled to welcome you on board.'
        self.source = settings.EMAIL_FROM
        self.to = user.email
    
    def send(self):
        # Wrapper in order to ease interchangibility
        send_email_wrapper(self.subject, self.body, self.source, self.to)
