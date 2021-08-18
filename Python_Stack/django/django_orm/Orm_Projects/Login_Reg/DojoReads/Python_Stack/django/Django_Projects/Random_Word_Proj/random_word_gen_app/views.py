from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    random_word = get_random_string(length=14) 
    random ={
        'rword': random_word
    }

    if 'id' not in request.session:
        request.session['id'] = 1

    return render(request,'index.html', random)


def random(request):
    request.session['id'] += 1
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
# Create your views here.
