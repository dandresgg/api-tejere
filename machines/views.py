''' Machine views '''
from urllib.request import urlopen

from bs4 import BeautifulSoup
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from machines.models import Machine, Part, Sector
from machines.serializers import (MachineSerializer, PartSerializer,
                                  SectorSerializer)


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

    @action(detail=False, methods=['GET'])
    def machine_sector(self, request) -> Response:
        ''' Get sectors by machine id '''
        m_id = request.query_params.get('m_id')
        machine = Machine.objects.get(id=m_id)
        sectors = Sector.objects.filter(machine=machine)
        if sectors:
            response = []
            for sector in sectors:
                response.append(SectorSerializer(sector).data)
            return Response(response, status=status.HTTP_200_OK)
        return Response('false', status=status.HTTP_400_BAD_REQUEST)


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

    @action(detail=False, methods=['GET'])
    def sector_part(self, request):
        ''' Get parts by sector id '''
        s_id = self.request.query_params.get('s_id')
        sector = Sector.objects.get(id=s_id)
        parts = Part.objects.filter(sector=sector)
        response = []
        if parts:
            for part in parts:
                response.append(PartSerializer(part).data)
            return Response(response, status=status.HTTP_200_OK)
        return Response('false', status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def id_from_reference(self, request):
        ''' Get parts by reference and sector '''
        ref = self.request.query_params.get('ref')
        sector = self.request.query_params.get('sector')
        part = Part.objects.filter(sector=sector, reference=ref)
        if part:
            return Response(part[0].id, status=status.HTTP_200_OK)
        return Response('Elemento no encontrado', status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_trm(self, request):
        ''' Get trm related Dolar and Colombian Pesos '''
        url = "https://www.dolar-colombia.com/"
        with urlopen(url) as html_page:
            bs_site = BeautifulSoup(html_page, "html.parser")
            elems = bs_site.find_all(
                "span", {"class": "exchange-rate exchange-rate_up"})
            for elem in elems:
                trm = elem.get_text()
                if trm:
                    return Response(trm, status=status.HTTP_200_OK)
        return Response('Elemento no encontrado', status=status.HTTP_200_OK)
