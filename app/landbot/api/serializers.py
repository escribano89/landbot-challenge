from rest_framework import serializers
from landbot.models import ExtendedUser


class ExtendedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = (
            'email', 'first_name', 'phone', 'origin'
        )
