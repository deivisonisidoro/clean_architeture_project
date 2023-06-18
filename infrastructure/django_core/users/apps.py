from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Configuration class for the 'users' app.

    This class defines the configuration for the 'users' app, including the app's name and the default
    auto-generated field for models. It serves as the entry point for configuring the app-specific settings.
    Attributes:
        default_auto_field (str): The default auto-generated field to be used for models.
        name (str): The name of the 'users' app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
