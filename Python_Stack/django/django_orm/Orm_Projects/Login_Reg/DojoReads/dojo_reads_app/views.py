from django.db import models
from django.shortcuts import render, redirect
from login_reg_app.models import User

def home(request):
    context = {
        'user': User.objects.get(id=request.session['log_user_id'])
    }

    return render(request, 'home.html', context)
# Create your views here.
