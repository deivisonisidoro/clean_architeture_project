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