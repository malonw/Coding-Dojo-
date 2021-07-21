from django.shortcuts import render, HttpResponse 

def index(request):
        return render(request, "index.html")

def results(request):
        # if request == "POST":
    context = {
            "name":request.POST["name"],
            "Dojo":request.POST["Dojo"],
            # "favorite":request.POST["favorite"],
            "comments":request.POST["comments"],
        }
    return render(request, "results.html", context)

# Create your views here.
