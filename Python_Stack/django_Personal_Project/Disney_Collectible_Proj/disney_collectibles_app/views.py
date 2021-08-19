from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import User, Catagory, Manufacturer, Item
import bcrypt


def index(request):
    form = RegisterForm()
    context = {'regForm': form}
    return render(request, 'index.html', context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect ('/home')
        messages.error(request, "Unsuccessful Registration. Invalid information.")
    form = RegisterForm
    return redirect('/index')
        


# def register(request):
#     if request.method == "GET":
#         return redirect("/landing")
#     if request.method == "POST":
#         errors = User.objects.user_validator(request.POST)
#         user1 = User.objects.filter(email=request.POST['email'])
#         if user1.exists():
#             messages.error(
#                 request, "This email is already Registered!", extra_tags='register')
#             return redirect('/')

#         if len(errors) > 0:
#             for key, value in errors.items():
#                 messages.error(request, value, extra_tags=key)
#             return redirect('/')
#         else:
#             user1 = User.objects.create(
#                 fname=request.POST['fname'],
#                 lname=request.POST['lname'],
#                 email=request.POST['email'],
#                 password=bcrypt.hashpw(
#                     request.POST['password'].encode(), bcrypt.gensalt()).decode()
#             )
#             request.session['log_user_id'] = user1.id
#         return redirect('/')

#     return redirect("/")
# # login


# def login(request):
#     user_list = User.objects.filter(email=request.POST['email'])
#     if user_list:
#         logged_user = user_list[0]
#         if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
#             request.session['log_user_id'] = logged_user.id

#             return redirect('/home')
#         else:
#             messages.error(request, "Invalid email or password.",
#                            extra_tags='login')
#             return redirect('/')
#     messages.error(request, "Email does not exist.", extra_tags='login')
#     return redirect('/')

# logout


def logout(request):
    request.session.clear()
    return redirect('/')

# Create your views here.


@login_required(login_url='/')
def home(request):

    context = {
        'user': User.objects.get(id=request.session['log_user_id']),

    }

    return render(request, 'home.html', context)
