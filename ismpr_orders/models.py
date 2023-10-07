from django.db import models
import ismpr_worker.models as worker_models
import ismpr_client.models as client_models


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование статуса')

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
                                        related_name='ClientOrder',
                                        verbose_name='Оборудование клиента')

    typeService = models.ForeignKey(TypeService,
                                    on_delete=models.CASCADE,
                                    related_name='ClientOrder',
                                    verbose_name='Тип сервиса')

    client = models.ForeignKey(client_models.Client,
                               on_delete=models.CASCADE,
                               related_name='ClientOrder',
                               verbose_name='Клиент')

    worker = models.ForeignKey(worker_models.Worker,
                               on_delete=models.CASCADE,
                               related_name='ClientOrder',
                               verbose_name='Работник принявший заявку')

    orderStatus = models.ForeignKey(OrderStatus,
                                    on_delete=models.CASCADE,
                                    related_name='ClientOrder',
                                    verbose_name='Текущий статус заявки')

    DateOrder = models.DateField(verbose_name='Дата выполнения заявки')

    class Meta:
        verbose_name = 'Заявка клиента'
        verbose_name_plural = 'Заявки клиентов'