from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Show


def tvshows(request):
    context = {
        'all_shows': Show.objects.all()
    }

    return render(request, 'tvshows.html', context)


def new(request):
        errors = Show.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/create')
    
        else:

            Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release_date'],
                descript=request.POST['descript'],
            )
            messages.success(request, 'TV Show Created')
            # Show.objects.last()
        return redirect('/tvshows')

def create(request):
    return render(request, 'create.html')


def edit(request, id):
    edit_query = {
        'shows': Show.objects.get(id=id)
    }
    return render(request, 'edit.html', edit_query)


def update(request, id):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect (id +'/edit/')
    else:
        update = Show.objects.get(id=id)
        update.title = request.POST['title']
        update.network = request.POST['network']
        update.release_date = request.POST['release_date']
        update.descript = request.POST['descript']
        update.save()
        messages.success(request, 'TV Show Updated')

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
