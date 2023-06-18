from django.db import transaction
from pydantic.dataclasses import dataclass
from users.models.user import User

from src.application.users.dto import UserDTO
from src.application.users.interfaces.repository_interface import UserRepositoryInterface


@dataclass
class UseRepository(UserRepositoryInterface):
    """
    Implementation of UserRepositoryInterface that interacts with the database to perform user-related operations.
    """

    @transaction.atomic
    def create(self, user_dto: UserDTO):
        """
        Create a new user in the database.

        Args:
            user_dto (UserDTO): The data transfer object containing user information.
        """
        user = User.objects.create(
            username=user_dto.username,
            email=user_dto.email,
            password=user_dto.password,
        )
        user.save()
