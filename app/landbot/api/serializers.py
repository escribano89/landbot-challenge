from rest_framework import serializers
from landbot.models import ExtendedUser, Notification


class ExtendedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = (
            'email', 'first_name', 'phone', 'origin'
        )


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'user_id', 'notification'
        )
