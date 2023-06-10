from django.db import transaction
from pydantic.dataclasses import dataclass
from users.models.user import User

from src.application.users.dto import UserDTO
from src.application.users.interfaces.repository_interface import UserRepositoryInterface


@dataclass
class UseRepository(UserRepositoryInterface):
    @transaction.atomic
    def create(self, user_dto: UserDTO):
        user = User.objects.create(
            username=user_dto.username,
            email=user_dto.email,
            password=user_dto.password,
        )
        user.save()
