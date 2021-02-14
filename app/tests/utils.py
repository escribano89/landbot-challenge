from landbot.models import ExtendedUser


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
