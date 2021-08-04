from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages


def index(request):
    return render(request, 'index.html')




# Create your views here.
