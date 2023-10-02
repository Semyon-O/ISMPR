from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")
    Address = models.TextField()
    Phone = models.CharField(max_length=12)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.client.save()


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


