from rest_framework import serializers
from .models import ClientOrders, OrderStatus, TypeService
from ismpr_client.serializers import ClientShowEquipmentSerializer
from ismpr_worker.serializers import WorkerBaseSerializers


class TypeServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeService
        fields = ('id', 'name')


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ('id', 'name')


class OrderSerializerInfo(serializers.ModelSerializer):
    clientEquipment = ClientShowEquipmentSerializer()
    typeService = TypeServiceSerializer()
    orderStatus = OrderStatusSerializer()
    worker = WorkerBaseSerializers()

    class Meta:
        model = ClientOrders
        fields = ('id', 'clientEquipment', 'typeService', 'client', 'worker', 'orderStatus', 'DateOrder')
        read_only_fields = ('client', 'orderStatus')

    @staticmethod
    def convert_instance_to_text(instance):
        data = {}
        data['clientEquipment'] = instance.clientEquipment.__str__()
        data['typeService'] = instance.typeService.__str__()
        data['client'] = instance.client.__str__()
        return data


class OrderSerializerUpdateCreate(serializers.ModelSerializer):
    class Meta:
        model = ClientOrders
        fields = ('id', 'clientEquipment', 'typeService', 'client', 'worker', 'orderStatus', 'DateOrder')