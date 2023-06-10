from pydantic import EmailStr
from pydantic.dataclasses import dataclass

from src.domain.users.entities.user_entity import UserEntity


@dataclass
class UserDTO:
    username: str
    email: EmailStr
    password: str

    def to_domain(self):
        user_entity = UserEntity(self.username, self.email, self.password)

        return user_entity

    def to_dto(self, user_entity: UserEntity):
        return UserDTO(username=user_entity.username, email=user_entity.email, password=user_entity.password)
