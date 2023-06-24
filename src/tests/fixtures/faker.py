import pytest
from faker import Faker


@pytest.fixture
def fake():
    """
    Fixture providing a Faker instance.

    This fixture creates and returns an instance of the Faker class, which
    can be used to generate fake data for testing purposes.

    Returns:
        Faker: An instance of the Faker class.
    """
    return Faker()
