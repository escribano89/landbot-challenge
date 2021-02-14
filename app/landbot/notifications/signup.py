from django.conf import settings

STRATEGIES = {
    'email': {
        'subject': 'Welcome to Landbot!',
        'from': settings.EMAIL_FROM,
        'body': 'The entire team of Landbot is thrilled to welcome you on board.'
    }
}
