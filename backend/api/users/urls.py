from django.urls import path
from .views import UserInfosView

urlpatterns = [
    path("user-info/", UserInfosView.as_view(), name="user-info"),
]
