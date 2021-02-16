from landbot.notifications.sales import Sales
from landbot.notifications.pricing import Pricing
from landbot.notifications.signup import Signup

# Map between the topic and
# the lowercase notification
TOPIC_CHANNELS_MAPPING = {
    'sales': Sales,
    'pricing': Pricing,
    'signup': Signup,
}
