from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login),
    path("forgot_password/", views.forgot_password_view),
]   