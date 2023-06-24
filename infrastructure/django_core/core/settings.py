"""
Django project settings.

Configures various aspects of your Django project, such as the database, installed apps,
middleware, templates, and more.

For more information on each setting, refer to the Django documentation.

Attributes:
    BASE_DIR (Path): The base directory of the Django project.
    SECRET_KEY (str): The secret key used for cryptographic signing.
    DEBUG (bool): Determines whether the project is in debug mode.
    ALLOWED_HOSTS (list): The list of allowed host names.
    INSTALLED_APPS (list): The list of installed Django applications.
    MIDDLEWARE (list): The list of middleware classes.
    ROOT_URLCONF (str): The Python module containing the project's URL patterns.
    REST_FRAMEWORK (dict): Configuration options for the Django REST Framework.
    TEMPLATES (list): The list of Django template configurations.
    WSGI_APPLICATION (str): The Python module containing the project's WSGI application.
    DATABASES (dict): Database configuration settings.
    AUTH_PASSWORD_VALIDATORS (list): The list of password validation rules.
    LANGUAGE_CODE (str): The default language code.
    TIME_ZONE (str): The default time zone.
    USE_I18N (bool): Determines whether internationalization is enabled.
    USE_TZ (bool): Determines whether time zones are used.
    STATIC_URL (str): The URL prefix for static files.
    DEFAULT_AUTO_FIELD (str): The default primary key field type.
    AUTH_USER_MODEL (str): The custom user model used for authentication.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = (
    "django-insecure-a5_^wcu127zdctb=&p%uvma9y2ga%-@bazd5vh!#e$#ak5)6t-"
)

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"]
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"
