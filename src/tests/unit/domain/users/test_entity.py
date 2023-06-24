from faker import Faker
from pydantic import EmailStr

from src.domain.users.entity import UserEntity


class TestUserEntity:
    """
    Test class for the UserEntity entity.
    """

    def test_user_entity_creation(self, fake: Faker):
        """
        Test UserEntity creation without an ID.

        This test method verifies the creation of a UserEntity object without
        specifying an ID. It uses fake data to initialize the attributes of
        UserEntity and asserts the correctness of the attributes.

        Args:
            fake (Fake): The fixture providing the Faker instance.
        """
        username = fake.user_name()
        email = EmailStr(fake.email())
        password = fake.password()
        user_entity = UserEntity(
            username=username,
            email=email,
            password=password,
        )
        assert user_entity.username == user_entity.username
        assert user_entity.email == user_entity.email
        assert user_entity.password == user_entity.password
        assert user_entity.id is None

    def test_user_entity_creation_with_id(self, fake: Faker):
        """
        Test UserEntity creation with an ID.

        This test method verifies the creation of a UserEntity object with
        a specified ID. It uses fake data to initialize the attributes of
        UserEntity along with an ID and asserts the correctness of the attributes.

        Args:
            fake (Faker): The fixture providing the Faker instance.
        """
        user_id = fake.random_int()

        user_entity = UserEntity(
            username=fake.user_name(),
            email=EmailStr(fake.email()),
            password=fake.password(),
            id=user_id,
        )

        assert user_entity.username == user_entity.username
        assert user_entity.email == user_entity.email
        assert user_entity.password == user_entity.password
        assert user_entity.id == user_id
