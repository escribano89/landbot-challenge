from django.urls import path

from landbot.api.views import CreateUserAPIView, RequestAssistance

urlpatterns = [
    path(
        'users/',
        CreateUserAPIView.as_view(),
        name='create-user'
    ),
    path(
        'users/assistance/',
        RequestAssistance.as_view(),
        name='user-assistance'
    )
]
