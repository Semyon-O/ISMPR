from rest_framework import serializers
from ismpr_orders.models import ClientOrders, OrderStatus, TypeService
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


class OrderSerializerInfo(serializers.Serializer):
    id = serializers.IntegerField()
    clientEquipment = serializers.SerializerMethodField()
    typeService = serializers.SerializerMethodField()
    orderStatus = serializers.SerializerMethodField()
    worker = serializers.SerializerMethodField()
    DateOrder = serializers.DateField()

    # class Meta:
    #     model = ClientOrders
    #     fields = ('id', 'clientEquipment', 'typeService', 'client', 'worker', 'orderStatus', 'DateOrder')
    #     read_only_fields = ('client', 'orderStatus')
    def get_clientEquipment(self, obj):
        return {
            'id': obj.clientEquipment.id,
            'name': obj.clientEquipment.Name,
            'typeEquipment': obj.clientEquipment.typeEquipment.type,
        }

    def get_typeService(self, obj):
        return {
            'id': obj.typeService.id,
            'name': obj.typeService.name
        }

    def get_worker(self, obj):
        try:
            return {
                'id': obj.worker.id,
                'first_name': obj.worker.user.first_name,
                'last_name': obj.worker.user.last_name,
                'phone': obj.worker.Phone,
            }
        except AttributeError:
            return None

    def get_orderStatus(self, obj):
        return {
            'id': obj.orderStatus.id,
            'name': obj.orderStatus.name
        }


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
        fields = ('id', 'clientEquipment', 'typeService', 'worker', 'DateOrder')