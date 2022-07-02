from rest_framework import serializers
from machines.models import Part

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Order
        fields = ('id', 'user', 'number', 'bill',
                  'data_json', 'state', 'send', 'created')

    def create(self, validated_data):
        parts = validated_data['data_json']
        for j_part in parts:
            if j_part['qty'] > 0:
                part = Part.objects.get(id=j_part['id'])
                part.stock = part.stock - j_part['qty']
                part.save()
        return super().create(validated_data)
