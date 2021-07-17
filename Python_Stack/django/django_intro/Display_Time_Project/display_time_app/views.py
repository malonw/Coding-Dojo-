from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse ("It Works")


# Create your views here.
