from abc import ABC, abstractmethod

from src.application.users.dto import UserDTO
from src.application.users.interfaces.repository_interface import (
    UserRepositoryInterface,
)
from src.domain.users.entities.user_entity import UserEntity


class UserServiceInterface(ABC):
    """Interface for creating a user."""

    storage: UserRepositoryInterface

    @abstractmethod
    def create_user(self, user_dto: UserDTO) -> UserEntity:
        pass
