import re
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "GET":
        return redirect("/index.html")
    if request.method == "POST":
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email='email').exists():
                messages.error(request, "You have already Registered!")
                return redirect('/')
            else:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    hash1=bcrypt.hashpw(
                        password.encode(), bcrypt.gensalt()).decode()
                )
                return redirect('/success')

        else:
            messages.error(request, "Password do not match. Try again.")
        return redirect("/")
    return redirect("/")


def validate_login(request):
    user = User.objects.filter(email='email')
    if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
        print("Passwords match!")
        return redirect('/login')
    else:
        print("Failed Password")
        return redirect('/')


def login(request):
    if User.objects.filter(email=request.POST['email']).exists():
        logged_user = User.objects.get(id=id)

        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['email'] = logged_user.id
            return redirect('/success')

    return redirect('/')


def success(request):
    if request.method == "GET":
        return redirect('/')
    # temporary
    context = {
        'all': User.objects.all()
    }
    return render(request, 'success.html', context)
# Create your views here.
