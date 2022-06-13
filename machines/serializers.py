from rest_framework import serializers

from machines.models import Machine, Part, Sector


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('id', 'name', 'kind')


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('id', 'machine', 'kind', 'img')


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'sector', 'description', 'code',
                  'reference', 'price', 'img', 'stock')
