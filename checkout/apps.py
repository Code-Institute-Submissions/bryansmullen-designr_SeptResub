# flake8: noqa
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    This class defines the config object for the app
    """
    name = 'checkout'

    # do not delete this import - this is essential for updating orders total
    def ready(self):
        import checkout.signals
