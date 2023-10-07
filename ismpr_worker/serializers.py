from rest_framework import serializers
from .models import Worker, WorkerStatus
from django.contrib.auth.models import User


class WorkerBaseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ('username', 'Phone', 'workerStatus', 'Company')


class AuthWorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')