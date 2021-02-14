from celery import shared_task
from django.core.mail import send_mail


@shared_task
def signup_notification(email):
    send_mail(
        'Landbot Subject here',
        'Here is the message.',
        'from@example.com',
        [email],
        fail_silently=False,
    )
