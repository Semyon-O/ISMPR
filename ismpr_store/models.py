from django.db import models


class Manufactor(models.Model):
    id_business = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)


class SpareParts(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    manufactor = models.ForeignKey(to=Manufactor, related_name="spare_part", on_delete=models.CASCADE)


class Store(models.Model):
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = models.CharField(max_length=10)
    time = models.CharField(max_length=50)
    spare_parts = models.ManyToManyField(to=SpareParts, related_name='stores', through="SparePartsInStore")


class SparePartsInStore(models.Model):
    store = models.ForeignKey(to=Store, on_delete=models.CASCADE)
    spare_parts = models.ForeignKey(to=SpareParts, on_delete=models.CASCADE)
    amount = models.IntegerField()

