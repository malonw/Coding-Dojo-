"""Disney_Collectible_Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin

from disney_collectibles_app.models import User as U, Catagory, Manufacturer, Item


class UAdmin(admin.ModelAdmin):
    pass


admin.site.register(U, UAdmin)


class CatagoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Catagory, CatagoryAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Manufacturer, ManufacturerAdmin)


class ItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('disney_collectibles_app.urls'))
]
