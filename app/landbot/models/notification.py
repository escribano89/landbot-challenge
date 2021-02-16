from django.db import models
from landbot.models import ExtendedUser


class Notification(models.Model):
    user = models.ForeignKey(
        ExtendedUser,
        on_delete=models.CASCADE,
    )
    notification = models.CharField(max_length=120)
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Notification to {} through {}'.format(
            self.user.email, self.strategy
        )
