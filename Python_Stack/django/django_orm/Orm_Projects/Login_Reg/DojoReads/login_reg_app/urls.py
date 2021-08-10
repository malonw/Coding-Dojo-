from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login_reg_app/register', views.register),
    path('login_reg_app/login', views.login),
    path('login_reg_app/logout', views.logout),
    path('login_reg_app/redirect_view', views.redirect_view),

]
