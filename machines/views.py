from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

from machines.models import Machine, Sector
from machines.serializers import MachineSerializer, SectorSerializer


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )


class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )
