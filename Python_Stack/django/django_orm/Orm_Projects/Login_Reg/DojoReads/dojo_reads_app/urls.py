from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('add_book', views.add_book),
    path('new_book',views.new_book),
    
]
