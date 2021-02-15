from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ExtendedUser(AbstractUser):
    """Extended the AbstractUser to add more properties to the base one"""

    phone = PhoneNumberField(max_length=64)
    origin = models.CharField(max_length=32)
    first_name = models.CharField(max_length=64)
    # Added email as unique
    email = models.EmailField(unique=True)
    # Removed username as we're going to use the email field
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone', 'origin']

    def __str__(self):
        return self.email

