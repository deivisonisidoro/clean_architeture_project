import pytest
from faker import Faker

from src.application.users.dto import UserDTO
from src.domain.users.entity import UserEntity


class TestUserDTO:
    def test_user_dto_creation(self, fake: Faker):
        """Test the creation of a UserDTO instance.

        This test verifies that a UserDTO instance is created with the expected attribute values.

        Args:
            fake (Faker): An instance of the Faker class for generating fake data.

        """
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        user_dto = UserDTO(username, email, password)

        assert user_dto.username == username
        assert user_dto.email == email
        assert user_dto.password == password

    def test_user_dto_to_domain(self, fake: Faker):
        """Test the to_domain method of the UserDTO class.

        This test verifies that the to_domain method correctly converts a UserDTO object to a UserEntity object.

        Args:
            fake (Faker): An instance of the Faker class for generating fake data.

        """
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        user_dto = UserDTO(username, email, password)
        user_entity = user_dto.to_domain()

        assert user_entity.username == username
        assert user_entity.email == email
        assert user_entity.password == password

    def test_user_dto_to_dto(self, fake: Faker):
        """Test the to_dto method of the UserDTO class.

        This test verifies that the to_dto method correctly converts a UserEntity object to a UserDTO object.

        Args:
            fake (Faker): An instance of the Faker class for generating fake data.

        """
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        user_entity = UserEntity(
            username=username,
            email=email,
            password=password,
        )

        user_dto = UserDTO(username, email, password)
        user = user_dto.to_dto(user_entity)

        assert user.username == username
        assert user.email == email
        assert user.password == password

    def test_user_dto_invalid_email(self, fake: Faker):
        """Test the creation of an invalid UserDTO instance with an invalid email.

        This test verifies that an invalid UserDTO instance is not created when an invalid email is provided.

        Args:
            fake (Faker): An instance of the Faker class for generating fake data.
        """
        username = fake.user_name()
        invalid_email = "invalid_email"
        password = fake.password()

        with pytest.raises(ValueError):
            UserDTO(username, invalid_email, password)
