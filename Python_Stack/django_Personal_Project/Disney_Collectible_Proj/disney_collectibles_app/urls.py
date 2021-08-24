from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
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
