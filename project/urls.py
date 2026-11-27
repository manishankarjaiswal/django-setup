"""URL configuration for project."""

from django.contrib import admin
from django.urls import path

from project.views import health_check

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check, name="health_check"),
]
