from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('gold_generator',views.gold_generator),

]