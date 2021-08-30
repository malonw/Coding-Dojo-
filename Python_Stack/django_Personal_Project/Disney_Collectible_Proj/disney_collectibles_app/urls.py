from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('', views.dashboard),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", views.dashboard, name="dashboard"),
    url(r"^register/", views.register, name="register"),
    url(r"^password_reset/", views.password_reset, name="password_reset"),
    path("add_item", views.add_item, name="add_item"),
    path("create", views.create, name="create"),
    path("edit/<int:item_id>", views.edit),
    path("update/<int:item_id>", views.update),
    path("favorites/<int:item_id>", views.favorite),
    path("my_favorites/<int:user_id>", views.my_favorites),
    path("view_all", views.view_all),
    path("view_one/<int:item_id>", views.view_one),
    path("remove/<int:item_id>", views.remove),
]
