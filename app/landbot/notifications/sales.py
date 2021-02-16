from django.conf import settings
import requests


class Sales():

    def __init__(self, user):
        # User is mandatory for the sales notification
        if not user:
            raise(Exception)

        self.message = 'sales.slack'
        self.user = user

    def send(self):
        message = "Request sales assistance by: {}".format(self.user.email)
        payload = '{"text":"%s"}' % message
        requests.post(settings.SLACK_WEBHOOK, data=payload)
