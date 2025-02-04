from django.urls import path
from .views import UserInfosView, UserRegistrationView

urlpatterns = [
    path("user-info/", UserInfosView.as_view(), name="user-info"),
    path("register/", UserRegistrationView.as_view(), name="register-user"),
]
