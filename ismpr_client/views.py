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

from .serializers import UserSerializer, AuthUserSerializer, ClientEquipmentSerializer, TypeEquipmentSerializer


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
                "token": f"TOKEN {authed_user.auth_token}"
            })
        except ObjectDoesNotExist:
            return Response({"message": "Client does not exist"}, status=status.HTTP_404_NOT_FOUND)


class EquipmentClientViewSet(ModelViewSet):
    queryset = ClientEquipment.objects.all()
    serializer_class = ClientEquipmentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user.client)

    def perform_update(self, serializer):
        serializer.save(client=self.request.user.client)

    def get_queryset(self):
        return ClientEquipment.objects.all().filter(client=self.request.user.client)


class TypeEquipmentView(generics.ListAPIView):
    queryset = TypeEquipment.objects.all()
    serializer_class = TypeEquipmentSerializer
