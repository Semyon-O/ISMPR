from rest_framework import serializers
from . import models


class SparePartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SpareParts
        fields=["id", "name", "description"]


class StoreInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Store
        fields = ['id', "address", 'latitude', 'longitude', 'phone', 'time']


class SparePartsInStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SparePartsInStore
        fields = ["id", "spare_parts", 'amount']