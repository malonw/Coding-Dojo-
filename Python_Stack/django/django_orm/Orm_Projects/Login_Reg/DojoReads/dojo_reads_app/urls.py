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
    path('book_details_review/<int:book_id>', views.book_details_review),
    path('user_info/<int:user_id>', views.user_info),
    path('destroy/<int:user_id>', views.destroy),
    path('update/<int:user_id>', views.update_review),



]
