from django.urls import path
from .views import ResgisterViewAPi, LoginViewApi

urlpatterns = [
    path("register/", ResgisterViewAPi.as_view(), name="register"),
    path("login/", LoginViewApi.as_view(), name="login"),

]
