from typing import Any

from pydantic import EmailStr
from pydantic.dataclasses import dataclass


@dataclass(init=True)
class UserEntity:
    """
    Entity class representing a user.

    This class represents a user entity with attributes such as id, username,
    email, and password. It is used to store and manipulate user data within
    the application.

    Attributes:
        id (Any): The unique identifier of the user.
        username (str): The username of the user.
        email (EmailStr): The email address of the user.
        password (str): The password of the user.

    Methods:
        __init__: Initializes a new UserEntity object.

    """

    id: Any
    username: str
    email: EmailStr
    password: str

    def __init__(
        self, username: str, email: EmailStr, password: str, id: Any = None
    ):
        """
        Initializes a new UserEntity object.

        Args:
            username (str): The username of the user.
            email (EmailStr): The email address of the user.
            password (str): The password of the user.
            id (Any, optional): The unique identifier of the user. Defaults to None.

        """
        self.id = id
        self.username = username
        self.email = email
        self.password = password
