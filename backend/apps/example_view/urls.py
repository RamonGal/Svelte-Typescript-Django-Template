from .views import example_view
from django.urls import path

urlpatterns = [
    path("example/", example_view, name="example_view"),
]