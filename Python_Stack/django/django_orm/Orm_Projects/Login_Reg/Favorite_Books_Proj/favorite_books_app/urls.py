from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('register', views.register),
    path('redirect-success', views.books),
    path('login', views.login),
    path('logout', views.logout),
    path('redirect_view', views.redirect_view),
    path('update/<int:id>', views.update),
    path('edit/<int:id>', views.edit),

]
