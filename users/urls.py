from django.urls import path
from .views import UserListView
from .views import (
    ForgotPasswordView,
    LoginView,
    ProfileView,
    RegisterView,
    UserListView,
   
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
    path("login/", LoginView.as_view(), name="user-login"),
    path("profile/", ProfileView.as_view(), name="user-profile"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="user-forgot-password"),
    path("", UserListView.as_view(), name="user-list"),
    path("", UserListView.as_view(), name="user-list"),
]
