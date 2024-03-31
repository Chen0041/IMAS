from django.urls import path

from . import views
from .user_info import login_views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", login_views.login),
]