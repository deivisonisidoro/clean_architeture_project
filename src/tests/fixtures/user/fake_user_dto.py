import pytest
from faker import Faker

from src.application.users.dto import UserDTO


@pytest.fixture
def fake_user_dto(fake: Faker):
    """
    Fixture that generates a fake `UserDTO` object for testing purposes.

    Args:
        fake (Faker): The Faker object used for generating fake data.

    Returns:
        user_dto  (UserDTO): The generated `UserDTO` object with fake data.
    """
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    return UserDTO(username, email, password)
