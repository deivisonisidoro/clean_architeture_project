from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from infrastructure.django_core.users.views import UserViewSet

router = routers.DefaultRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
"""
URL configuration for the Django project.

Defines the URL patterns for the project, including routes to the admin site and API
endpoints.

URL Patterns:
    - `/admin/`: URL route for the Django admin site.
    - `/api/`: URL route for the REST API endpoints.

UserViewSet:
    - `users/`: URL route for user-related API endpoints.

Note:
    Make sure to include this module in the project's ROOT_URLCONF settings.
"""
