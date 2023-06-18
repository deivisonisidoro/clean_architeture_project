from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.
    """

    def create_user(self, username, email, password=None):
        """
        Creates and saves a new user.

        Args:
            username (str): The username of the user.
            email (str): The email address of the user.
            password (str, optional): The password for the user. Defaults to None.

        Returns:
            user (User): The created user object.
        """
        if not username:
            raise ValueError("O campo 'username' é obrigatório.")
        if not email:
            raise ValueError("O campo 'email' é obrigatório.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a new superuser.

        Args:
            username (str): The username of the superuser.
            email (str): The email address of the superuser.
            password (str, optional): The password for the superuser. Defaults to None.

        Returns:
            user (User): The created superuser object.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
