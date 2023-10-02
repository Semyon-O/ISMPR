from django.contrib.auth.models import User
from .models import ClientEquipment
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from .serializers import UserSerializer, AuthUserSerializer, ClientEquipmentSerializer


class RegisterNewUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer

    def create(self, request, *args, **kwargs):
        return Response("OK") # TODO: Реализовать получение Token


class EquipmentClientView(ListAPIView, CreateAPIView):
    queryset = ClientEquipment.objects.all()
    serializer_class = ClientEquipmentSerializer