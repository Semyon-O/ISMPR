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

    list_display_admin = ('id', 'client', 'Name', 'typeEquipment', 'Company', 'Description')
    list_display_client = ('id', 'Name', 'typeEquipment', 'Company', 'Description')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # если пользователь суперпользователь, показываем все объекты
        return qs.filter(client__user=request.user)  # фильтруем объекты по пользователю

    def save_model(self, request, obj, form, change):
        if not obj.client_id:  # если объект еще не сохранен
            obj.client = Client.objects.get(user=request.user)
        super().save_model(request, obj, form, change)

    def get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display_admin  # Показываем все колонки для администратора
        return self.list_display_client  # Показываем определенные колонки для клиента