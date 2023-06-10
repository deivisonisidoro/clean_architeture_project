from typing import Any

from pydantic import EmailStr
from pydantic.dataclasses import dataclass


@dataclass
class UserEntity:
    """User model.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (EmailStr): The email address of the user.
    """

    id: Any
    username: str
    email: EmailStr
    password: str

    def __init__(
        self, username: str, email: EmailStr, password: str, id: Any = None
    ):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
