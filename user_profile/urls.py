from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from user_profile.views import ProfileViewSet


router = routers.DefaultRouter()
router.register('profile', ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
