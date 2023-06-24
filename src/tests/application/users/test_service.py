import pytest

from src.domain.enums.error_message import ErrorMessage
from src.domain.enums.status_code import StatusCode
from src.domain.enums.success_message import SuccessMessage


class TestUserService:
    """
    Unit tests for the UserService class.

    Attributes:
        user_service (UserService): An instance of the UserService class.
        fake_user_dto (UserDTO): A fake UserDTO object for testing.
    """

    def test_create_user_success(self, user_service, fake_user_dto):
        """
        Test case for creating a user successfully.

        It verifies that the UserService.create_user method returns a dictionary with
        the expected success message and status code.

        Args:
            user_service (UserService): An instance of the UserService class.
            fake_user_dto (UserDTO): A fake UserDTO object.


        """
        result = user_service.create_user(fake_user_dto)

        assert "message" in result
        assert "code" in result
        assert result["message"] == SuccessMessage.CREATED_SUCCESSFULLY.value
        assert result["code"] == StatusCode.CREATED.value

    def test_create_user_failure(self, user_service, fake_user_dto):
        """
        Test case for creating a user with a failure.

        It simulates a failure in the storage.create method and verifies that the
        UserService.create_user method returns a dictionary with the expected error
        message and status code.

        Args:
            user_service (UserService): An instance of the UserService class.
            fake_user_dto (UserDTO): A fake UserDTO object.


        """
        user_service.storage.create = pytest.raises(Exception)

        result = user_service.create_user(fake_user_dto)

        assert "message" in result
        assert "code" in result
        assert result["message"] == ErrorMessage.INVALID_REQUEST.value
        assert result["code"] == StatusCode.BAD_REQUEST.value
