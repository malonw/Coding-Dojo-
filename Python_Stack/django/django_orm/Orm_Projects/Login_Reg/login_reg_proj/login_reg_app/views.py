from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.sav()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect("indext.html")
        messages.error(
            request, "Unsuccessful Registration. Invalid Information.")
    form = NewUserForm
    return render(request=request, template_name="register.html", context={"register_form": form})


# Create your views here.
