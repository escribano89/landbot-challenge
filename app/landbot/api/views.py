from rest_framework import generics

from landbot.api.serializers import ExtendedUserSerializer, NotificationSerializer
from landbot.notifications.mapping import TOPIC_CHANNELS_MAPPING
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = ExtendedUserSerializer


class RequestAssistance(APIView):
    def post(self, request, format=None):
        provided_topic = request.POST.get('topic', None)

        if provided_topic is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = NotificationSerializer(
            data=request.data
        )