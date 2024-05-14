from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import AuthWorkerSerializer


class AuthWorkerView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthWorkerSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')

        authed_user = authenticate(username=username, password=password)

        if authed_user is None:
            return Response({"message": "Error Authentication"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            worker_id = authed_user.worker.id
            return Response({
                "worker_id": worker_id,
                "firstName": authed_user.first_name,
                "lastName": authed_user.last_name,
                "email": authed_user.email,
                "token": f"Token {authed_user.auth_token}",

            })
        except ObjectDoesNotExist:
            return Response({"message": "Worker does not exist"}, status=status.HTTP_404_NOT_FOUND)