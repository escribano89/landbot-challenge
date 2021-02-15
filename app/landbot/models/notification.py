from django.db import models


class Notification(models.Model):
    notification = models.CharField(max_length=120)
    customer_email = models.EmailField()
    strategy = models.CharField(max_length=60)
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['notification', 'strategy', 'customer_email']

    def __str__(self):
        return 'Notification to {} through {}'.format(
            self.user.email, self.strategy
        )
