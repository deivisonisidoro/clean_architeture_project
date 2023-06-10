from rest_framework import viewsets
from rest_framework.response import Response
from users.models import User

from infrastructure.django_core.users.repository import UseRepository
from src.application.users.dto import UserDTO
from src.application.users.service import UserService


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def create(self, request):
        dto = UserDTO(**request.data)
        repository = UseRepository()
        service = UserService(repository)
        response = service.create_user(dto)
        return Response({"detail": response["message"]}, status=response["code"])
