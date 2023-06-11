from pydantic import EmailStr
from pydantic.dataclasses import dataclass

from src.domain.users.entity import UserEntity


@dataclass
class UserDTO:
    """
    Data Transfer Object (DTO) representing user data.

    It is used for transferring user data between different layers of the application,
    such as from the presentation layer to the domain layer.

    Attributes:
        username (str): The username of the user.
        email (EmailStr): The email address of the user.
        password (str): The password of the user.
    """

    username: str
    email: EmailStr
    password: str

    def to_domain(self):
        """Converts the UserDTO to a UserEntity object.

        Returns:
            user_entity (UserEntity): The UserEntity object representing the user.
        """
        user_entity = UserEntity(self.username, self.email, self.password)

        return user_entity

    def to_dto(self, user_entity: UserEntity):
        """Converts a UserEntity object to a UserDTO.

        Args:
            user_entity (UserEntity): The UserEntity object to convert.

        Returns:
            user_dto (UserDTO): The UserDTO object representing the user.
        """
        return UserDTO(
            username=user_entity.username,
            email=user_entity.email,
            password=user_entity.password,
        )
