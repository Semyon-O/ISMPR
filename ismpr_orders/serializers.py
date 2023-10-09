from rest_framework import serializers
from .models import ClientOrders


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientOrders
        fields = ('id', 'clientEquipment', 'typeService', 'client', 'worker', 'orderStatus', 'DateOrder')

