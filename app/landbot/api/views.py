from rest_framework import generics

from landbot.api.serializers import (
    ExtendedUserSerializer,
    NotificationSerializer,
    AssistanceSerializer,
)
from landbot.notifications.mapping import TOPIC_CHANNELS_MAPPING
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from landbot.models import ExtendedUser


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = ExtendedUserSerializer


class RequestAssistance(APIView):
    def post(self, request):
        serializer = AssistanceSerializer(data=request.data)
        if serializer.is_valid():
            return self.save_notification(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def save_notification(self, data):
        user = ExtendedUser.objects.filter(email=data['email']).first()
        notification_dict = {
            'notification': TOPIC_CHANNELS_MAPPING.get(data['topic']),
            'user': user.id
        }
        serializer = NotificationSerializer(
            data=notification_dict
        )
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
