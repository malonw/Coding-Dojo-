from django.urls import path
from login_reg_app import views
from . import views

urlpatterns = [
    path('', views.index),
]
