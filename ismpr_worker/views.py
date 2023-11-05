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
                "message": "OK",
                "worker_id": worker_id,
                "token": f"TOKEN {authed_user.auth_token}"
            })
        except ObjectDoesNotExist:
            return Response({"message": "Worker does not exist"}, status=status.HTTP_404_NOT_FOUND)