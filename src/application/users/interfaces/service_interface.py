from abc import ABC, abstractmethod

from src.application.users.dto import UserDTO
from src.application.users.interfaces.repository_interface import (
    UserRepositoryInterface,
)
from src.domain.users.entity import UserEntity


class UserServiceInterface(ABC):
    """
    Interface for UserService classes that manage users.

    This interface defines the contract for UserService classes that handle user-related operations,
    such as creating a new user. Classes implementing this interface should provide an implementation
    for the `create_user` method.

    Attributes:
        storage (UserRepositoryInterface): The repository interface for user data storage.

    """

    storage: UserRepositoryInterface

    @abstractmethod
    def create_user(self, user_dto: UserDTO) -> UserEntity:
        """
        Create a new user based on the provided UserDTO and return the UserEntity.

        This method takes a UserDTO object containing the user data, creates a new user
        using the data, and returns the corresponding UserEntity object.

        Args:
            user_dto (UserDTO): The UserDTO object containing the user data.

        Returns:
            UserEntity: The created UserEntity object representing the new user.

        """
        pass
