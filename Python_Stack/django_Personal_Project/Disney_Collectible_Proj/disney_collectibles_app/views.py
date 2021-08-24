from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages  # import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Item, Manufacturer, Catagory
import bcrypt


def homepage(request):

    return render(request=request, template_name='main/home.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            User.objects.create(
                First_Name=request.POST['First_Name'],
                Last_Name=request.POST['Last_Name'],
                email=request.POST['email'],
            )
            return redirect("main:homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    return render(request=request, template_name="main/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:homepage")


def add_item(request):
    return render(request, template_name='add_item.html')


def create(request):
    if request.method == "POST":
        user1 = request.user.id
        if len(request.POST['new_prod_man']) > 0:
            man = Manufacturer.objects.create(
                mname=request.POST['new_prod_man']
            )
        else:
            man = Manufacturer.objects.get(id=request.POST['prod_man'])

        Catagory.objects.create(
            cname=request.POST['prod_cat'],
        )

        Item.objects.create(
            name=request.POST['name'],
            desc=request.POST['desc'],
            quantity=request.POST['quantity'],
            value=request.POST['value'],
            image=request.POST['image'],
            prod_man=man,
            # prod_cat=cat

        )
        add_fav = Item.objects.last()
        if add_fav.favorite.filter(id=user1).exists():
            add_fav.favorite.remove(user1)
        else:
            add_fav.favorite.add(user1)

    return redirect('/add_item')


def edit(request, item_id):
    context = {
        'user': User.objects.get(id=request.user.id),
        'item': Item.objects.get(id=item_id),

    }
    return render(request, 'edit.html', context)


def update(request, item_id):
    update = Item.objects.get(id=item_id)
    if request.method == "POST":

        update.name = request.POST['name'],
        update.desc = request.POST['desc'],
        update.quantity = request.POST['quantity'],
        update.value = request.POST['value'],
        update.image = request.POST['image'],
        update.save()
        messages.success(
            request, 'Item Successfully Updated', extra_tags='update')

    return redirect(f'/edit/{item_id}')


def favorite(request, item_id):
    user = request.user.id
    add_fav = Item.objects.get(id=item_id)
    if add_fav.favorite.filter(id=user).exists():
        add_fav.favorite.remove(user)
    else:
        add_fav.favorite.add(user)
    return redirect('/view_all')


def my_favorites(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),

    }
    return render(request, 'my_favorites.html', context)


def view_all(request):
    context = {
        'all': Item.objects.all()
    }
    return render(request, 'view_all.html', context)


def view_one(request, item_id):
    context = {
        'item': Item.objects.get(id=item_id),

    }
    return render(request, 'view_one.html', context)


def remove(request, item_id):
    if request.method == "POST":
        messages.warning(
            request, "Are you sure you want to delete this Item :{item.name}?")
        dele = Item.objects.get(id=item_id)
        dele.delete()
    return redirect('/home')
