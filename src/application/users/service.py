from pydantic.dataclasses import dataclass

from src.application.users.dto import UserDTO
from src.application.users.interfaces.repository_interface import UserRepositoryInterface
from src.application.users.interfaces.service_interface import UserServiceInterface
from src.domain.enums.error_message import ErrorMessage
from src.domain.enums.status_code import StatusCode
from src.domain.enums.success_message import SuccessMessage


@dataclass
class UserService(UserServiceInterface):
    """
    Service class for managing users.

    Attributes:
        storage (UserRepositoryInterface): The repository interface for user storage.
        success_message (SuccessMessage): Enum class containing success messages.
        error_message (ErrorMessage): Enum class containing error messages.
    """

    storage: UserRepositoryInterface
    success_message = SuccessMessage
    error_message = ErrorMessage

    def create_user(self, user_dto: UserDTO):
        """Create a new user.

        Args:
            user_dto (UserDTO): The user data transfer object.

        Returns:
            dictionary (dict): A dictionary with a success message.

        Raises:
            (Exception): A dictionary with an error message.

        """
        user_entity = user_dto.to_domain()
        try:
            dto = user_dto.to_dto(user_entity)
            self.storage.create(dto)
            return {
                "message": self.success_message.CREATED_SUCCESSFULLY.value,
                "code": StatusCode.CREATED.value,
            }

        except Exception:
            return {
                "message": self.error_message.INVALID_REQUEST.value,
                "code": StatusCode.BAD_REQUEST.value,
            }
