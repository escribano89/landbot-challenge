from rest_framework import serializers
from landbot.models import ExtendedUser, Notification
from landbot.notifications.mapping import TOPIC_CHANNELS_MAPPING


class ExtendedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = (
            'email', 'first_name', 'phone', 'origin'
        )


class AssistanceSerializer(serializers.Serializer):
    topic = serializers.CharField(required=True, max_length=60)
    email = serializers.EmailField(required=True)

    def validate_topic(self, data):
        if data.lower() not in TOPIC_CHANNELS_MAPPING.keys():
            raise serializers.ValidationError("Provided topic is not valid")
        return data

    def validate_email(self, data):
        if not ExtendedUser.objects.filter(email=data.lower()).exists():
            raise serializers.ValidationError("Provided email is not registered")
        return data


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'user', 'notification'
        )
