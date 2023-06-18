from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone

from .user_manager import UserManager


class User(AbstractBaseUser):
    """
    Custom user model representing a user in the system.

    Attributes:
        username (str): The unique username of the user.
        email (str): The unique email address of the user.
        is_active (bool): A flag indicating if the user account is active.
        is_admin (bool): A flag indicating if the user has administrative privileges.
        created_at (datetime): The timestamp when the user account was created.
        USERNAME_FIELD (str): The field used for authentication, in this case, 'username'.
        EMAIL_FIELD (str): The field used for the email address, in this case, 'email'.
        REQUIRED_FIELDS (list): The required fields when creating a user, in this case, ['email'].
        objects (UserManager): The manager class for the User model.

    Methods:
        __str__(): Returns a string representation of the user (the username).
        has_perm(perm, obj=None): Checks if the user has a specific permission (always True for admin users).
        has_module_perms(app_label): Checks if the user has permissions to access a specific app (always True for admin users).
    """

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
