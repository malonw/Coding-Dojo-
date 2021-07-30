from django.shortcuts import render, redirect
from .models import Show

def shows(request):
    context = {
        'all_shows':Show.objects.all()
        }
    
    return render(request, 'shows.html', context)

def new(request):
    if request.POST == "POST":
        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['netwrok'],
            release_date=request.POST['release_date'],
            descript=request.POST['descript']
            )
    return render(request, 'create.html')

def update(request):
    if request.method == "POST":
        if Show.objects.get(id=request.POST["id"]):
            Show.save()
            return render(request, 'read.html')
    return render(request, 'edit.html')

def read_one(request):
        if request.method == 'GET':
            if Show.objects.get(id=request.POST["id"]):
                return render (request, 'read.html')        
        return render(request, 'read.html')

def delete(request):
    if request.method == 'POST':
        if Show.objects.get(id=request.POST["id"]):
            Show.delete()
        return redirect("/")
    else:
        return redirect ("/")
# Create your views here.
