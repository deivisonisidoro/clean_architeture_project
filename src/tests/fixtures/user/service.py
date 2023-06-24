import pytest

from src.application.users.interfaces.repository_interface import UserRepositoryInterface
from src.application.users.service import UserService


class MockUserRepository(UserRepositoryInterface):
    """
    Mock implementation of UserRepositoryInterface.

    This class provides a mock implementation of the UserRepositoryInterface
    for testing purposes.

    """

    def create(self, user_dto):
        pass


@pytest.fixture
def user_service():
    """
    Fixture that provides a `UserService` object with a mocked `UserRepositoryInterface`.

    Returns:
      user_service  (UserService): The `UserService` object with a mocked `UserRepositoryInterface`.
    """
    repository = MockUserRepository()
    return UserService(repository)
