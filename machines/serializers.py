''' Machine serializers '''
from rest_framework import serializers

from machines.models import Machine, Part, Sector


class MachineSerializer(serializers.ModelSerializer):
    ''' Serializer machine model '''
    class Meta:
        model = Machine
        fields = ('id', 'name', 'kind')


class SectorSerializer(serializers.ModelSerializer):
    ''' Serializer sector model '''
    class Meta:
        model = Sector
        fields = ('id', 'machine', 'kind', 'img')


class PartSerializer(serializers.ModelSerializer):
    ''' Serializer part model '''
    class Meta:
        model = Part
        fields = ('id', 'sector', 'description', 'code',
                  'reference', 'price', 'img', 'photo', 'stock', 'url_seller')
