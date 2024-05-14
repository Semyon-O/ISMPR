from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class InfoAboutStore(generics.ListAPIView):
    queryset = models.Store.objects.all()
    serializer_class = serializers.StoreInfoSerializer

    def list(self, request, *args, **kwargs):
        query_objects = self.get_queryset()
        serialized_objects = serializers.StoreInfoSerializer(query_objects, many=True)
        return Response(serialized_objects.data)


class RetrieveConcreteStore(generics.RetrieveAPIView):
    queryset = models.Store.objects.all()
    serializer_class = serializers.StoreInfoSerializer


class RetrieveAllSparePartsByConcreteStore(generics.RetrieveAPIView):
    serializer_class = serializers.SparePartsInStoreSerializer

    def get_queryset(self):
        return models.SparePartsInStore.objects.filter(store=self.kwargs.get("pk"))

    def retrieve(self, request, *args, **kwargs):
        spare_parts = self.get_queryset()
        serialized_data = []
        for spare_part in spare_parts:
            spare_part_object = serializers.SparePartsInStoreSerializer(spare_part)
            serialized_data.append(spare_part_object.data)
        return Response(data=serialized_data)
