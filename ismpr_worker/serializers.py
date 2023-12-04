from rest_framework import serializers

from ismpr_client.serializers import UserSerializer
from .models import Worker, WorkerStatus
from django.contrib.auth.models import User


class WorkerBaseSerializers(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Worker
        fields = ('user', 'Phone', 'workerStatus', 'Company')


class AuthWorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')