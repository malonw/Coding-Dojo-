from django.urls import path
from . import views

urlpatterns = [
    path('', views.tvshows),
    path('tvshows', views.tvshows),
    path('create', views.new),
    path('<int:id>/edit', views.edit),
    path('<int:id>/update', views.update),
    path('read/<int:id>', views.read_one),
    path('<id>/delete', views.delete),
]