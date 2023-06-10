from pydantic.dataclasses import dataclass

from src.application.users.dto import UserDTO
from src.application.users.interfaces.repository_interface import UserRepositoryInterface
from src.application.users.interfaces.service_interface import UserServiceInterface
from src.domain.users.entities.user_entity import UserEntity
from src.domain.users.enums import ErrorMessage, SuccessMessage


@dataclass
class UserService(UserServiceInterface):
    storage: UserRepositoryInterface
    success_message = SuccessMessage
    error_message = ErrorMessage

    def create_user(self, user_dto: UserDTO) -> UserEntity:
        user_entity = user_dto.to_domain()
        try:
            dto = user_dto.to_dto(user_entity)
            self.storage.save(dto)
            return {"message": self.success_message.CREATED_SUCCESSFULLY.value, "code": 201}

        except Exception:
            return {"message": self.error_message.INVALID_REQUEST.value, "code": 400}
