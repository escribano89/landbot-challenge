from rest_framework import generics

from landbot.api.serializers import ExtendedUserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = ExtendedUserSerializer
