from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import OrderSerializer
from .models import ClientOrders


class OrderViewSet(ModelViewSet):
    queryset = ClientOrders.objects.all()
    serializer_class = OrderSerializer