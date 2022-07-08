''' User_profile admin panel '''
from django.contrib import admin

from user_profile.models import Profile

admin.site.register(Profile)
