from django.contrib import admin
from .models import Client, User, TypeEquipment, ClientEquipment


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'Address', 'Phone')
    list_editable = ('Address', 'Phone')


@admin.register(TypeEquipment)
class TypeEquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'description')
    list_editable = ('type', 'description')


@admin.register(ClientEquipment)
class ClientEquipmentAdmin(admin.ModelAdmin):
    list_display = ('id','client', 'Name', 'typeEquipment', 'Company', 'Description')
    list_editable = ('Name', 'typeEquipment', 'Company', 'Description')