from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from .models import ClientEquipment
from rest_framework.generics import CreateAPIView, ListAPIView
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


class EquipmentClientViewSet(ModelViewSet):
    queryset = ClientEquipment.objects.all()
    serializer_class = ClientEquipmentSerializer