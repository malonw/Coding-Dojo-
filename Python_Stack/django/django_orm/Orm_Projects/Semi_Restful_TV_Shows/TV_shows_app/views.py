from django.shortcuts import render, redirect
from .models import Show


def tvshows(request):
    context = {
        'all_shows': Show.objects.all()
    }

    return render(request, 'tvshows.html', context)


def new(request):
    if request.POST == "POST":
        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['netwrok'],
            release_date=request.POST['release_date'],
            descript=request.POST['descript']
        )
    return render(request, 'create.html')




def edit(request, id):
    edit_query = {
        'shows': Show.objects.get(id=id)
    }
    return render(request, 'edit.html', edit_query)


def update(request, id):
    update = Show.objects.get(id=id)
    update.title = request.POST['title'],
    update.network = request.POST['netwrok'],
    update.release_date = request.POST['release_date'],
    update.descript = request.POST['descript'],
    update.save()
    return redirect('/')


def read_one(request, id):
    show_query = {
        'shows': Show.objects.get(id=id)
    }
    return render(request, 'read.html', show_query)



def delete(request, id):
    dele=Show.objects.get(id=id)
    dele.delete()
    return redirect('/')
