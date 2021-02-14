from landbot.models import ExtendedUser
from landbot.models import Notification
from unittest import mock


def create_and_validate_custom_user(
    first_name='Javier', email='test@test.test', phone='+41524204242', origin='landbot'
):
    with mock.patch('landbot.models.extended_user.async_notification', return_value=''):
        user = ExtendedUser.objects.create(
            email=email,
            first_name=first_name,
            phone=phone,
            origin=origin,
        )

        user.set_unusable_password()
        user.clean_fields()
        return user


def create_and_validate_custom_notification(
    notification='welcome_message', strategy='email', user=None
):
    notification = Notification.objects.create(
        notification=notification,
        strategy=strategy,
        user=user,
    )

    notification.clean_fields()
    return notification
