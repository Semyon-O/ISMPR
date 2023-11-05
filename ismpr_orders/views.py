from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer, OrderStatusSerializer, TypeServiceSerializer
from .models import ClientOrders, OrderStatus, TypeService, RejectedOrders

from ismpr_client.models import Client


class OrderViewSet(ModelViewSet):
    queryset = ClientOrders.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        client: Client = self.request.user.client
        order_status_base = OrderStatus.objects.get(id=1)
        serializer.save(client=client, orderStatus=order_status_base)

    def perform_destroy(self, instance: ClientOrders):
        user = self.request.user
        reason = self.request.data.pop('reason')
        new_rejected = RejectedOrders(ReasonDescription=reason,
                                      whoRejected=user,
                                      InfoOrder=self.serializer_class.convert_instance_to_text(instance))
        new_rejected.save()
        instance.delete()


class TypeServiceView(generics.ListAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class OrderStatusView(generics.ListAPIView):
    queryset = TypeService.objects.all()
    serializer_class = TypeServiceSerializer