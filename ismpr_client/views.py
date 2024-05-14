from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

from .models import ClientEquipment, TypeEquipment
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import (UserSerializer, AuthUserSerializer,
                          ClientShowEquipmentSerializer,
                          TypeEquipmentSerializer, ClientEquipmentSerializer)

from django.http import HttpResponse


def start_page(request):

    return HttpResponse("Здравствуйте, многоуважаемые ребята группы Н11")


class RegisterNewUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')

        authed_user = authenticate(username=username, password=password)

        if authed_user is None:
            return Response({"message": "Error Authentication"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            client_id = authed_user.client.id
            return Response({
                    "client_id": client_id,
                    "token": f"TOKEN {authed_user.auth_token}",
                    "first_name": authed_user.first_name,
                    "last_name": authed_user.last_name,
                    'email': authed_user.email,
            })
        except ObjectDoesNotExist:
            return Response({"message": "Client does not exist"}, status=status.HTTP_404_NOT_FOUND)


class EquipmentClientViewSet(ModelViewSet):
    queryset = ClientEquipment.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ClientEquipmentSerializer
        return ClientShowEquipmentSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user.client)

    def perform_update(self, serializer):
        serializer.save(client=self.request.user.client)

    def get_queryset(self):
        return ClientEquipment.objects.all().filter(client=self.request.user.client)


class TypeEquipmentView(generics.ListAPIView):
    queryset = TypeEquipment.objects.all()
    serializer_class = TypeEquipmentSerializer
