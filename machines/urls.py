''' Machines urls '''
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from machines.views import MachineViewSet, PartViewSet, SectorViewSet

router = routers.DefaultRouter()
router.register('part', PartViewSet)
router.register('main', MachineViewSet)
router.register('sector', SectorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
