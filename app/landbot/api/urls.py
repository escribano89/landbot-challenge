from django.urls import path

from landbot.api.views import CreateUserAPIView, RequestAssistance

urlpatterns = [
    path(
        'user/create/',
        CreateUserAPIView.as_view(),
        name='create-user'
    ),
    path(
        'user/assistance/',
        RequestAssistance.as_view(),
        name='user-assistance'
    )
]
