from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('add_book', views.add_book),
    path('new_book', views.new_book),
    path('book_review/<int:book_id>', views.book_review),
    path('user_info/<int:user_id>', views.user_info),
    path('destroy/<int:book_id>', views.destroy),
    path('add_review', views.add_a_review),



]
