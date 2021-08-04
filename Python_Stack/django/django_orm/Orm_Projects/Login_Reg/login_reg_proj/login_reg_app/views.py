from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import User




def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "GET":
        return redirect("/index.html")
    if request.method == "POST":
        if request.session['email'] == User.objects.filter('email'):
            return HttpResponse("You have already Registered!")
        else:
            password = request.POST['password']
            User.objects.create(
                fname = request.POST['fname'],
                lname = request.POST['lname'],
                email = request.POST['email'],
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            )
    return redirect('/success')

def success(request):
    return render(request, 'success.html')
# Create your views here.
