import factory
from landbot.models import ExtendedUser, Notification
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


@factory.django.mute_signals(signals.post_save)
def create_and_validate_custom_notification(
    notification='signup', strategy='email', customer_email='customer@test.test'
):
    notification = Notification.objects.create(
        notification=notification,
        strategy=strategy,
        customer_email=customer_email,
    )

    notification.clean_fields()
    return notification
