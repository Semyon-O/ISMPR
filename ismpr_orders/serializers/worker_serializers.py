from rest_framework import serializers


class WorkerOrderSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    client = serializers.SerializerMethodField()
    DateOrder = serializers.DateField()
    clientEquipment = serializers.SerializerMethodField()
    typeService = serializers.SerializerMethodField()
    problemDescription = serializers.CharField()

    def get_client(self, obj):
        return {
            'id': obj.client.id,
            'first_name': obj.client.user.first_name,
            'last_name': obj.client.user.last_name,
            'Address': obj.client.Address,
            'Phone': obj.client.Phone,
        }

    def get_clientEquipment(self, obj):
        return {
            'type': obj.clientEquipment.typeEquipment.type,
            'Name': obj.clientEquipment.Name,
            'Company': obj.clientEquipment.Company
        }

    def get_typeService(self, obj):
        return {
            'name': obj.typeService.name
        }