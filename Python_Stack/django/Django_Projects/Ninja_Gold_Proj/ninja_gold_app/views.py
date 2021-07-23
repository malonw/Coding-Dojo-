from django.shortcuts import render, redirect
import random
from time import localtime, strftime


def index(request):
    request.session ["total_gold"] = 0
    request.session ["activites"] = []
    return render(request, "index.html")

def gold_generator(request):
    if request.method == "POST":
        if request.POST['action'] == "farm":
            total = random.randint(10,20)
            request.session["total_gold"] += total
            request.session["activities"].append('Received ' + str(total) + ' gold from the farm!('+ strftime("%a, %d %b %Y %H:%M %p")+')', localtime())
            
        elif request.POST['action'] == "cave":
            total = random.randint(5,10)
            request.session["total_gold"] += total
            request.session["activities"].append('Received ' + str(total) + ' gold from the cave!('+ strftime("%a, %d %b %Y %H:%M %p")+')', localtime())
            
        elif request.POST["action"] == "house":
            total = random.randint(2,5)
            request.session["total_gold"] += total
            request.session["activities"].append('Received ' + str(total) + ' gold from the house!('+ strftime("%a, %d %b %Y %H:%M %p")+')', localtime())
            
        elif request.POST["action"] == "casino":
            total = random.randint(-50,50)
            request.session["total_gold"] += total
            if total > 0:
                request.session["activities"].append('Entered a Casino and won ' + str(total) + ' gold!('+ strftime("%a, %d %b %Y %H:%M %p")+')', localtime())
            else:
                request.session["activities"].append('Entered a Casino and lost ' + str(total) + ' gold!('+ strftime("%a, %d %b %Y %H:%M %p")+')', localtime())
            
    else:
        return redirect('/')


