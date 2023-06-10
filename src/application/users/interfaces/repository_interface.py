from abc import ABC, abstractclassmethod

from pydantic.dataclasses import dataclass

from src.application.users.dto import UserDTO


@dataclass
class UserRepositoryInterface(ABC):
    @abstractclassmethod
    def create(self, user_dto: UserDTO):
        ...
