from django.shortcuts import render, HttpResponse 

def index(request):
        return render(request, "index.html")

def results(request):

    request.session["name"] = request.POST["name"]
    request.session["Dojo"]=request.POST["Dojo"]
    request.session["favorite"]=request.POST["favorite"]
    request.session["comments"]=request.POST["comments"]

    # context = {
    #         "name":request.POST["name"],
    #         "Dojo":request.POST["Dojo"],
    #         "favorite":request.POST["favorite"],
    #         "comments":request.POST["comments"],
    #     }
    return render(request, "results.html")

# Create your views here.
