from django.contrib import admin

from ismpr_worker.models import Worker
from .models import OrderStatus, ClientOrders, TypeService, RejectedOrders


@admin.register(ClientOrders)
class ClientOrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'clientEquipment', 'typeService', 'client', 'worker', 'orderStatus', 'DateOrder']
    list_editable = ['worker', 'orderStatus']
    list_filter = ['worker']

    def get_queryset(self, request):
        orders = super().get_queryset(request)
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return orders

            try:
                worker = Worker.objects.get(user=request.user)
                return orders.filter(worker=worker)
            except Exception:
                return orders.none()
        return orders.none()


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']


@admin.register(TypeService)
class TypeServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']


@admin.register(RejectedOrders)
class RejectedOrders(admin.ModelAdmin):
    list_display = ['id', 'whoRejected', 'ReasonDescription', 'InfoOrder']