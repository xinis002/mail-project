from django.urls import path

from .apps import UsersConfig
from .views import register, profile, CustomLoginView
from django.contrib.auth import views as auth_views

app_name = UsersConfig.name

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
