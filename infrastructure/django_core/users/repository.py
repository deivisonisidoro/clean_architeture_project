from django.db import transaction
from pydantic.dataclasses import dataclass
from users.models import User

from src.application.users.dto import UserDTO
from src.application.users.interfaces.repository_interface import UserRepositoryInterface


@dataclass
class UseRepository(UserRepositoryInterface):
    def _user_dto_to_model(self, user_dto: UserDTO):
        user = User()
        user.username = user_dto.username
        user.email = user_dto.email
        user.password = user_dto.password

        return user

    @transaction.atomic
    def save(self, user_dto: UserDTO):
        user = self._user_dto_to_model(user_dto)
        user.save()
