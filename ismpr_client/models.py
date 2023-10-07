from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")
    Address = models.TextField()
    Phone = models.CharField(max_length=12)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f"{self.user}"


class TypeEquipment(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f'{self.type.__str__()}'

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'


class ClientEquipment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    typeEquipment = models.ForeignKey(TypeEquipment, on_delete=models.CASCADE)
    Company = models.CharField(max_length=50)
    Description = models.TextField()

    def __str__(self):
        return f"{self.pk}: {self.client.__str__()} - {self.Name.__str__()}"

    class Meta:
        verbose_name = 'Оборудование Клиента'
        verbose_name_plural = 'Оборудование Клиентов'

