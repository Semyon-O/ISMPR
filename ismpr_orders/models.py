from django.contrib.auth.models import User
from django.db import models
import ismpr_worker.models as worker_models
import ismpr_client.models as client_models


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование статуса')
    isActiveStatus = models.BooleanField(verbose_name="Активный?", null=True)

    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'

    def __str__(self):
        return f'{str(self.name)}'


class TypeService(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип услуги')

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуги'

    def __str__(self):
        return f'{str(self.name)}'


class ClientOrders(models.Model):
    clientEquipment = models.ForeignKey(client_models.ClientEquipment,
                                        on_delete=models.CASCADE,
                                        verbose_name='Оборудование клиента')

    typeService = models.ForeignKey(TypeService,
                                    on_delete=models.CASCADE,
                                    verbose_name='Тип сервиса')

    client = models.ForeignKey(client_models.Client,
                               on_delete=models.CASCADE,
                               verbose_name='Клиент')

    worker = models.ForeignKey(worker_models.Worker,
                               on_delete=models.CASCADE,
                               verbose_name='Работник принявший заявку',
                               blank=True,
                               null=True
                               )

    orderStatus = models.ForeignKey(OrderStatus,
                                    on_delete=models.CASCADE,
                                    verbose_name='Текущий статус заявки')

    DateOrder = models.DateField(verbose_name='Дата выполнения заявки')

    problemDescription = models.TextField(verbose_name='Описание проблемы', null=True, blank=True)

    class Meta:
        verbose_name = 'Заявка клиента'
        verbose_name_plural = 'Заявки клиентов'


class RejectedOrders(models.Model):
    ReasonDescription = models.TextField(max_length=255, verbose_name="Причина отклонения", null=True)
    whoRejected = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь отменивший заявку")
    InfoOrder = models.TextField(null=True, blank=True, verbose_name="Информация о Заявке")

    class Meta:
        verbose_name = 'Отмененная заявка клиента'
        verbose_name_plural = 'Отмененные заявки клиентов'