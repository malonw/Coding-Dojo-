from django.shortcuts import render
from time import gmtime, localtime, strftime

def index(request):
    context = {
        "time": strftime("%a, %d %b %Y %H:%M %p", localtime())
    }
    return render(request, "index.html", context)


# Create your views here.
