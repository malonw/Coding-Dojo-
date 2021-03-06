from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "GET":
        return redirect("/index.html")
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        user1 = User.objects.filter(email=request.POST['email'])
        if user1.exists():
            messages.error(
                request, "This email is already Registered!", extra_tags='register')
            return redirect('/')

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            user1 = User.objects.create(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                email=request.POST['email'],
                password=bcrypt.hashpw(
                    request.POST['password'].encode(), bcrypt.gensalt()).decode()
            )
            request.session['log_user_id'] = user1.id
            return redirect('/redirect_view')

    return redirect("/")


def login(request):
    user_list = User.objects.filter(email=request.POST['email'])
    if user_list:
        logged_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['log_user_id'] = logged_user.id
            return redirect('/redirect_view')
        else:
            messages.error(request, "Invalid email or password.",
                           extra_tags='login')
            return redirect('/')
    messages.error(request, "Email does not exist.", extra_tags='login')
    return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')


def redirect_view(request):
    response = redirect('/dojo_reads_app/')
    return response


def success(request):
    context = {
        'user': User.objects.get(id=request.session['log_user_id'])
    }
    return render(request, 'success.html', context)
# Create your views here.
