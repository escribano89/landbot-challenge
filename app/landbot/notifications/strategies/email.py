from django.core.mail import send_mail


def send_email_wrapper(subject, body, source, target):
    """Sends the email using the django core"""

    send_mail(
        subject,
        body,
        source,
        [target],
        fail_silently=False
    )
