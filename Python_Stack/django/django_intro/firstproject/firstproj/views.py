from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("This would be a list of all blogs")
def new(request):
    return HttpResponse("Display a form to create a blog")
def create(request):
    return HttpResponse("Would redirect")
def intnumber(request):
    return HttpResponse("placeholder to displat blog:{number}")
def intnumberedit(request):
    return HttpResponse("Placeholder to edit blog {number}")
def intnumberdel(request):
    return HttpResponse("redirect to destroy")
# Create your views here.
