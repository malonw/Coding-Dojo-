from django.shortcuts import render
from .models import users

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, "index.html", context)




    # Create your views here.
