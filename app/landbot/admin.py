from django.contrib import admin

# Register your models here.
from landbot.models import ExtendedUser, Notification

admin.site.register(ExtendedUser)
admin.site.register(Notification)
