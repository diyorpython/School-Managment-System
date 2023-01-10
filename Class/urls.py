from django.urls import path, re_path
from .views import response

urlpatterns = [
    path("res/", response),
]