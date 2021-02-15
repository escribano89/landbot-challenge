import factory
from landbot.models import ExtendedUser, Notification
from unittest import mock
from django.db.models import signals


@factory.django.mute_signals(signals.post_save)
def create_and_validate_custom_user(
    first_name='Javier', email='test@test.test', phone='+41524204242', origin='landbot'
):
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
