# flake8: noqa
from django.apps import AppConfig

class CheckoutConfig(AppConfig):
    name = 'checkout'

    # do not delete this import - this is essential for updating orders total
    def ready(self):
        import checkout.signals
