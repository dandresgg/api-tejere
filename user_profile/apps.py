''' User_profile app '''
from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    ''' config default '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
