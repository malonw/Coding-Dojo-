from django.urls import path
# from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
    path('', views.index),
    path('c:/Users/Malon.FBCWINE/OneDrive/Documents/CodingDojo/Python_Stack_django/django_intro/firstproject/firstproj', views.new),
    path('c:/Users/Malon.FBCWINE/OneDrive/Documents/CodingDojo/Python_Stack_django/django_intro/firstproject/firstproj',views.create),
    path('c:/Users/Malon.FBCWINE/OneDrive/Documents/CodingDojo/Python_Stack_django/django_intro/firstproject/firstproj',views.intnumber),
    path('c:/Users/Malon.FBCWINE/OneDrive/Documents/CodingDojo/Python_Stack_django/django_intro/firstproject/firstproj',views.intnumberedit),
    path('c:/Users/Malon.FBCWINE/OneDrive/Documents/CodingDojo/Python_Stack_django/django_intro/firstproject/firstproj',views.intnumberdel),
]