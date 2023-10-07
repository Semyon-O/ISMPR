from django.contrib.auth import authenticate
from django.contrib.auth.models import User
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

        if authed_user is not None: #TODO: Добавить проверку на то что пользователь является работником
            token_user = authed_user.auth_token

            return Response({"message": "OK",
                             "worker_id": authed_user.worker.id,
                             "token": f"TOKEN {token_user}"})
        else:
            return Response({"message": "Error Authentication"}, status=status.HTTP_401_UNAUTHORIZED)