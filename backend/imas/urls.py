from django.urls import path

from .user_info import login_views

urlpatterns = [
    path("user/login", login_views.login),
]