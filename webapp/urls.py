from django.urls import path
from .views import (
    home,
    register,
    login,
    logout,
    dashboard,
    create_record,
    update_record,
    view_record,
    delete_record,
)

urlpatterns = [
    path("", home, name="index"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("create-record/", create_record, name="create-record"),
    path("update-record/<int:pk>", update_record, name="update-record"),
    path("record/<int:pk>", view_record, name="view-record"),
    path("delete_record/<int:pk>", delete_record, name="delete-record"),
]
