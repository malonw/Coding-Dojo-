from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('redirect_view', views.redirect_view),
    path('dojo_reads_app', views.index, name='dojo_reads_app'),

]
