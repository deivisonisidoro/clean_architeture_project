from abc import ABC, abstractclassmethod

from pydantic.dataclasses import dataclass

from src.application.users.dto import UserDTO


@dataclass
class UserRepositoryInterface(ABC):
    """
    Interface for UserRepository classes that handle user data storage.

    This interface defines the contract for UserRepository classes that are responsible for
    storing user data. Classes implementing this interface should provide an implementation
    for the `create` method.

    """

    @abstractclassmethod
    def create(self, user_dto: UserDTO):
        """
        Create a new user based on the provided UserDTO.

        This method takes a UserDTO object containing the user data and
        creates a new user in the underlying data storage.

        Args:
            user_dto (UserDTO): The UserDTO object containing the user data.

        """
        ...
