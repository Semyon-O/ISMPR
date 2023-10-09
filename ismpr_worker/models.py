from django.contrib.auth.models import User
from django.db import models


class WorkerStatus(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Статус работника'
        verbose_name_plural = 'Статусы работников'

    def __str__(self):
        return f'{self.status}'


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="worker")
    Phone = models.CharField(max_length=12)
    workerStatus = models.ForeignKey(WorkerStatus, on_delete=models.CASCADE, related_name="worker")
    Company = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return f'{self.user}: {str(self.workerStatus).capitalize()}'