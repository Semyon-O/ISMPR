from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ismpr_orders.serializers.client_serializers import OrderSerializerInfo, OrderStatusSerializer, TypeServiceSerializer, OrderSerializerUpdateCreate
from .models import ClientOrders, OrderStatus, TypeService, RejectedOrders
from ismpr_orders.serializers import worker_serializers
from ismpr_client.models import Client


class OrderViewSet(ModelViewSet):
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
        reason = self.request.data.get('reason')
        new_rejected = RejectedOrders(ReasonDescription=reason,
                                      whoRejected=user,
                                      InfoOrder=self.serializer_class.convert_instance_to_text(instance))
        new_rejected.save()
        instance.delete()


class ActiveClientOrders(generics.ListAPIView):
    queryset = ClientOrders.objects.all()
    serializer_class = OrderSerializerInfo
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        all_orders = ClientOrders.objects.all().filter(client=self.request.user.client)
        return all_orders.filter(orderStatus__isActiveStatus=True)


class TypeServiceView(generics.ListAPIView):
    queryset = TypeService.objects.all()
    serializer_class = TypeServiceSerializer


class OrderStatusView(generics.ListAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class WorkerOrdersViewSet(viewsets.ViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        orders = ClientOrders.objects.all().filter(worker_id=request.user.worker.id, DateOrder__gt=timezone.now().date())
        serializer = worker_serializers.WorkerOrderSerializer(orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        orders = ClientOrders.objects.all().filter(id=pk)
        data = OrderSerializerInfo(orders, many=True).data
        return Response(data)

    def update(self, request, pk=None):
        order: ClientOrders = get_object_or_404(ClientOrders, id=pk)
        order.worker = request.user.worker
        order.save()
        return Response(status=status.HTTP_200_OK, data={"status": "Updated successfully"})


class WorkerActiveOrder(generics.ListAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        orders = ClientOrders.objects.all().filter(worker_id=request.user.worker.id, orderStatus_id__in=[3])
        serializer = worker_serializers.WorkerOrderSerializer(orders, many=True)
        return Response(serializer.data)


class WorkerHistoryOrders(generics.ListAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        orders = ClientOrders.objects.all().filter(worker_id=request.user.worker.id, orderStatus_id__in=[4])
        serializer = worker_serializers.WorkerOrderSerializer(orders, many=True)
        return Response(serializer.data)


class WorkerTodayOrders(generics.ListAPIView):
    queryset = ClientOrders.objects.all()
    serializer_class = worker_serializers.WorkerOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        orders = ClientOrders.objects.all().filter(worker_id=request.user.worker.id, DateOrder=timezone.now().date())
        serializer = worker_serializers.WorkerOrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderInfoView(generics.RetrieveAPIView):
    queryset = ClientOrders.objects.all().filter()
    serializer_class = worker_serializers.WorkerOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        orders = ClientOrders.objects.all().filter(id=pk)
        serializer = worker_serializers.WorkerOrderSerializer(orders, many=True)
        return Response(serializer.data[0])