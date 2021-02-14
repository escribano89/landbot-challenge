from django.contrib import admin

# Register your models here.
from landbot.models import ExtendedUser

admin.site.register(ExtendedUser)
