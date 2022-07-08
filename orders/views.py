''' Order viewsets '''
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from machines.models import Part
from orders.models import Order
from user_profile.models import Profile

from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    ''' Order views base serializers '''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['GET'])
    def get_orders(self, request) -> Response:
        ''' Get orders from user id '''
        u_id = request.query_params.get('u_id')
        user = Profile.objects.get(pk=u_id)
        orders = Order.objects.filter(user=user)
        if orders:
            response = []
            for order in orders:
                response.append(OrderSerializer(order).data)
            return Response(response, status=status.HTTP_200_OK)
        return Response('false', status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        order = Order.objects.get(id=request.data)
        ls_orders = order.data_json
        for ls_order in ls_orders:
            if ls_order['qty'] > 0:
                part = Part.objects.get(id=ls_order['id'])
                part.stock = part.stock + ls_order['qty']
                part.save()
        return super().destroy(request, *args, **kwargs)
