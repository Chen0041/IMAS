from django.urls import path

from .user_info import user_info_views
from .auto_QA import auto_QA_views

urlpatterns = [
    path("user/login", user_info_views.login),
    path("user/register", user_info_views.user_register),
    path("user/modify", user_info_views.user_modify),

    path("models", auto_QA_views.get_trained_models),
    path('autuQA/<str:modelName>', auto_QA_views.upload_medical_archive),
]