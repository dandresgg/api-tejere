from rest_framework import serializers

from machines.models import Machine, Part, Sector


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('id', 'name', 'kind')


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('machine', 'kind', 'img')


class PartSerializer(serializers.ModelSerializer):
    sector_name = serializers.CharField(source='sector.kind')

    class Meta:
        model = Part
        field = ('sector_name', 'description', 'code',
                 'reference', 'price', 'img', 'stock')
