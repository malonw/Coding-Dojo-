from django.shortcuts import render, redirect
import random
from time import strftime


def index(request):
    if "total_gold" and "activities" not in request.session: 
        request.session ["total_gold"] = 0
        request.session ["activities"] = []
    return render(request, 'index.html')
    

def process_money(request):
    if request.method == "POST":
        if request.POST['action'] == "farm":
            total = random.randint(10,20)
            request.session["total_gold"] += total
            request.session["activities"].append(f"Received  {str(total)}  gold from the farm!({ strftime('%a, %d %b %Y %H:%M %p')}")
            
        elif request.POST['action'] == "cave":
            total = random.randint(5,10)
            request.session["total_gold"] += total
            request.session["activities"].append(f"Received  {str(total)}  gold from the cave!({ strftime('%a, %d %b %Y %H:%M %p')}")
            
        elif request.POST["action"] == "house":
            total = random.randint(2,5)
            request.session["total_gold"] += total
            request.session["activities"].append(f"Received  {str(total)}  gold from the house!({ strftime('%a, %d %b %Y %H:%M %p')}")
            
        elif request.POST["action"] == "casino":
            total = random.randint(-50,50)
            request.session["total_gold"] += total
            if total > 0:
                request.session["activities"].append(f"Entered a Casino and won {str(total)} gold!({ strftime('%a, %d %b %Y %H:%M %p')}")
            else:
                request.session["activities"].append(f"Entered a Casino and lost {str(total)} gold!({ strftime('%a, %d %b %Y %H:%M %p')}")
        return redirect('/')    
    else:
        return redirect('/')
def reset(request):
    request.session.flush()
    return redirect("/")
    

