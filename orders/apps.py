''' Order app '''
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    ''' Config default '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
