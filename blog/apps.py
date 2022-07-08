''' Blog app '''
from django.apps import AppConfig


class BlogConfig(AppConfig):
    ''' Config default '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
