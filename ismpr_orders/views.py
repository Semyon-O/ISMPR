from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializerInfo, OrderStatusSerializer, TypeServiceSerializer, OrderSerializerUpdateCreate
from .models import ClientOrders, OrderStatus, TypeService, RejectedOrders

from ismpr_client.models import Client


class OrderViewSet(ModelViewSet):

    """
    Данные API позволяют управлять заявками от лица пользователя.
    Требуется токен.
    """

    queryset = ClientOrders.objects.all()
    serializer_class = OrderSerializerInfo
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ClientOrders.objects.all().filter(client=self.request.user.client)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return OrderSerializerUpdateCreate
        return OrderSerializerInfo

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


class ActiveClientOrders(generics.ListAPIView):

    """
    Возвращает список активных заявок для работников.
    """

    queryset = ClientOrders.objects.all()
    serializer_class = OrderSerializerInfo
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        all_orders = ClientOrders.objects.all().filter(client=self.request.user.client)
        return all_orders.filter(orderStatus__isActiveStatus=True)


class TypeServiceView(generics.ListAPIView):

    """
    Возвращает список типов
    """

    queryset = TypeService.objects.all()
    serializer_class = TypeServiceSerializer


class OrderStatusView(generics.ListAPIView):

    """
    Возвращает список статусов
    """

    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer