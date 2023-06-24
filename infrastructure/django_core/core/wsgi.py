import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
"""
WSGI config for the Django project.

It exposes the WSGI callable as a module-level variable named `application`.

Note:
    Make sure to configure the `DJANGO_SETTINGS_MODULE` environment variable with the
    appropriate Django settings module (e.g., "core.settings").

Example:
    Set the `DJANGO_SETTINGS_MODULE` environment variable in your server configuration
    to point to the Django project's settings module:
    
    `DJANGO_SETTINGS_MODULE=core.settings`

    Then, use the `application` variable as the WSGI callable in your server
    configuration.

Note:
    This module is typically used for deploying Django applications using WSGI-compatible
    servers, such as Gunicorn or uWSGI.
"""
