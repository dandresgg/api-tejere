''' Order urls '''
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import OrderViewSet

router = routers.DefaultRouter()
router.register('manage', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
