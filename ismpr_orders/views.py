from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ismpr_orders.serializers.client_serializers import OrderSerializerInfo, OrderStatusSerializer, TypeServiceSerializer, OrderSerializerUpdateCreate
from .models import ClientOrders, OrderStatus, TypeService, RejectedOrders, Feedback
from ismpr_orders.serializers import worker_serializers
from ismpr_client.models import Client
from .serializers.feedback_serializer import FeedbackSerializer

from .filters import OrderFilter

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
        # print(self.request.query_params.get("order_status", None))
        if self.request.query_params.get("order_status"):
            return ClientOrders.objects.all().filter(client=self.request.user.client, orderStatus__in=[self.request.query_params.get("order_status")])

        return ClientOrders.objects.all().filter(client=self.request.user.client, orderStatus__in=[1,2,3])

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return OrderSerializerUpdateCreate
        return OrderSerializerInfo

    def perform_create(self, serializer):
        client: Client = self.request.user.client
        if not ClientOrders.objects.filter(
            typeService=self.request.data['typeService'],
            clientEquipment=self.request.data['clientEquipment']
        ).exists():
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


class FeedbackView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, **kwargs):
        if hasattr(request.user, 'client'):
            feedbacks = Feedback.objects.all().filter(order__client_id=request.user.client.id)
            serializer = FeedbackSerializer(feedbacks, many=True)
            return Response(serializer.data)

        if hasattr(request.user, 'worker'):
            ...

    def create(self, request, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=500)

        if Feedback.objects.all().filter(order_id=request.data.get('order')).exists():
            return Response(status=412, data={
                'message': 'Feedback is exists'
            })

        serializer.save()
        return Response(serializer.data, status=200)

