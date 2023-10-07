from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate

from .models import ClientEquipment
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import UserSerializer, AuthUserSerializer, ClientEquipmentSerializer


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

        if authed_user is not None:
            token_user = authed_user.auth_token

            return Response({"message": "OK",
                             "client_id": authed_user.client.id,
                             "token": f"TOKEN {token_user}"})
        else:
            return Response({"message": "Error Authentication"}, status=status.HTTP_401_UNAUTHORIZED)


class EquipmentClientViewSet(ModelViewSet):
    queryset = ClientEquipment.objects.all()
    serializer_class = ClientEquipmentSerializer