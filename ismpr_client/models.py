from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client", verbose_name="Логин клиента")
    Address = models.TextField(verbose_name="Адрес пользователя")
    Phone = models.CharField(max_length=12, verbose_name="Телефон клиента")

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.user.__str__()}'

    def __str__(self):
        return f"{self.user.__str__()}"


class TypeEquipment(models.Model):
    type = models.CharField(max_length=50, verbose_name="тип оборудования")
    description = models.TextField(verbose_name="Описание типа")

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'

    def __str__(self):
        return f'{self.type.__str__()}'


class ClientEquipment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    Name = models.CharField(max_length=50, verbose_name="Название оборудования")
    typeEquipment = models.ForeignKey(TypeEquipment, on_delete=models.CASCADE, verbose_name="Тип оборудования")
    Company = models.CharField(max_length=50, verbose_name="Компания выдавшая оборудование")
    Description = models.TextField(verbose_name="Описание оборудования")

    class Meta:
        verbose_name = 'Оборудование клиента'
        verbose_name_plural = 'Оборудования клиентов'

    def __str__(self):
        return f"{self.pk}: {self.client} - {self.Name}"

