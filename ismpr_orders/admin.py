from django.contrib import admin
from .models import OrderStatus, ClientOrders, TypeService, RejectedOrders


@admin.register(ClientOrders)
class ClientOrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'clientEquipment', 'typeService', 'client', 'worker', 'orderStatus', 'DateOrder']
    list_editable = ['worker', 'orderStatus']


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