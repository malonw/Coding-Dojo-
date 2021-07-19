from django.shortcuts import render
def index(request):
    return render(request, "index.html")
def submit(request):
    if request.method == "Post":
        val_from_name = request.POST["name"]
        
# Create your views here.
