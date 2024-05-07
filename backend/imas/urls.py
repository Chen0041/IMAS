from django.urls import path

from .user_info import user_info_views
from .data_preprocessing import upload_dataset_views,preprocessed_data_views
from .model_train import train_task_views, report_views
from .auto_QA import auto_QA_views
from .QA_platform import QA_platform_views


urlpatterns = [
    # user_info
    path("user/login", user_info_views.login),
    path("user/register", user_info_views.user_register),
    path("user/modify", user_info_views.user_modify),

    # data_preprocessing
    path("dataset/download/<str:dataset>", upload_dataset_views.download_dataset),
    path("dataset/delete/<str:dataset>", upload_dataset_views.delete_dataset),
    path("datasets", upload_dataset_views.get_datasets),
    path("dataset/upload", upload_dataset_views.upload_dataset),

    path("dataset/preprocessed", preprocessed_data_views.get_preprocessed_datasets),
    path("dataset/<str:dataset>/cases", preprocessed_data_views.get_cases),
    path("dataset/<str:dataset>/modify/<str:patient_name>", preprocessed_data_views.modify_case),
    path("loadPicture/<str:dataset>/<str:picture_name>", preprocessed_data_views.get_picture),

    # model_train
    path("model/datasetsLabeled",  train_task_views.get_labeled_datasets),
    path("model/category",  train_task_views.get_model_categories),
    path("model/train/<str:model_name>",  train_task_views.creat_train_task),

    path("model/reports", report_views.get_report),
    path("model/reports/download", report_views.download_reports),
    path("model/delete/<str:task_name>", report_views.delete_task),
    path("model/deleteFailed", report_views.delete_failed_task),

    # auto_QA
    path("autuQA/models", auto_QA_views.get_trained_models),
    path('autuQA/<str:model_name>', auto_QA_views.upload_medical_archive),

    # QA_platform
    path("loadPicture/<int:question_id>", QA_platform_views.get_picture),
    path("QAPlatform/departments", QA_platform_views.get_departments),
    path("QAPlatform/questions", QA_platform_views.get_questions),
    path("QAPlatform/question/new", QA_platform_views.new_question),
    path("QAPlatform/question/answer/<int:question_id>", QA_platform_views.answer_question),
    path("QAPlatform/question/delete/<int:question_id>", QA_platform_views.delete_question),
]
