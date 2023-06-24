from typing import Any

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from users.models.user import User

from infrastructure.django_core.users.repository import UseRepository
from src.application.users.dto import UserDTO
from src.application.users.interfaces.repository_interface import (
    UserRepositoryInterface,
)
from src.application.users.interfaces.service_interface import (
    UserServiceInterface,
)
from src.application.users.service import UserService


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for managing users."""

    queryset = User.objects.all()

    def __init__(
        self,
        user_service: UserServiceInterface = UserService,
        user_repository: UserRepositoryInterface = UseRepository(),
        **kwargs: dict[str, Any],
    ):
        """
        Initialize the UserViewSet.

        Args:
            user_service (UserServiceInterface): An instance of UserServiceInterface.
            user_repository (UserRepositoryInterface): An instance of UserRepositoryInterface.
            **kwargs (dict[str, Any]): Additional keyword arguments.
        """
        super().__init__(**kwargs)
        self.user_service = user_service
        self.user_repository = user_repository

    def create(self, request: Request):
        """
        Create a new user.

        Args:
            request (Request): The HTTP request object.

        Returns:
            response (Response): The HTTP response object.
        """
        dto = UserDTO(**request.data)
        service = self.user_service(self.user_repository())
        response = service.create_user(dto)
        return Response(
            {"detail": response["message"]}, status=response["code"]
        )
