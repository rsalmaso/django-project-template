from django.urls import path

from . import views

urlpatterns = [
    path("healthy", views.healthy, name="healthy"),
]
