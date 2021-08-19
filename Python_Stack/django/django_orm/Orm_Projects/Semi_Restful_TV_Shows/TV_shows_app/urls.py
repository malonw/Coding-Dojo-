from django.urls import path
from . import views

urlpatterns = [
    path('', views.tvshows),
    path('tvshows', views.tvshows),
    path('create', views.create),
    path('new', views.new),
    path('<id>/edit', views.edit),
    path('update/<id>', views.update),
    path('read/<id>', views.read_one),
    path('read/<id>/edit', views.edit),
    path('<id>/delete', views.delete),
]
