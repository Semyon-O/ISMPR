from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")
    Address = models.TextField()
    Phone = models.CharField(max_length=12)


class TypeEquipment(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f'{self.type.__str__()}'


class ClientEquipment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    typeEquipment = models.ForeignKey(TypeEquipment, on_delete=models.CASCADE)
    Company = models.CharField(max_length=50)
    Description = models.TextField()

    def __str__(self):
        return f"{self.pk}: {self.client.__str__()} - {self.Name.__str__()}"


class WorkerStatus(models.Model):
    status = models.CharField(max_length=50)


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="worker")
    Phone = models.CharField(max_length=12)
    workerStatus = models.ForeignKey(WorkerStatus, on_delete=models.CASCADE, related_name="worker")
    Company = models.CharField(max_length=255)

