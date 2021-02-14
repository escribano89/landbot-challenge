from django.db import models
from landbot.models import ExtendedUser


class Notification(models.Model):
    user = models.ForeignKey(
        ExtendedUser,
        on_delete=models.CASCADE,
        related_name='notifications',
    )

    notification = models.CharField(max_length=120)
    strategy = models.CharField(max_length=60)
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['notification', 'strategy', 'user_id']

    def __str__(self):
        return 'Notification to {} through {}'.format(
            self.user.email, self.strategy
        )
