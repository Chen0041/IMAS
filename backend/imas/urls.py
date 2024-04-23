from django.urls import path

from .user_info import user_info_views

urlpatterns = [
    path("user/login", user_info_views.login),
    path("user/register", user_info_views.user_register),
    path("user/modify", user_info_views.user_modify),
]