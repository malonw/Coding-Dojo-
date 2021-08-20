from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages  # import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Item, Manufacturer, Catagory
import bcrypt


def homepage(request):

    return render(request=request, template_name='main/home.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            user1 = User.objects.create(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                email=request.POST['email'],
                password=bcrypt.hashpw(
                    request.POST['password'].encode(), bcrypt.gensalt()).decode()
            )
            request.session['log_user_id'] = user1.id
            return redirect("main:homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:homepage")


def add_item(request):
    return render(request, template_name='add_item.html')


def create(request):
    if request.method == "POST":
        user1 = request.session['log_user_id']
        this_item = Item.objects.create(
            name=request.POST['name'],
            catsgory=request.POST['catagory'],
            desc=request.POST['desc'],
            quantity=request.POST['quantity'],
            value=request.POST['value'],
            manufacturer=request.POST['manufacturer'],

        )
    return redirect('add_item')
