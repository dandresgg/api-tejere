''' profile urls '''
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from user_profile.views import ProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('create', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
