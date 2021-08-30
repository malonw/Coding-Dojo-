from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import Manufacturer, Catagory, Item
from django.contrib.auth.models import User


def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect(reverse("dashboard"))


def password_reset(request):
    return render(request, 'password_change_form.html')

    # if request.method == "GET":
    #     return redirect("/")
    # if request.method == "POST":
    #     errors = User.objects.user_validator(request.POST)
    #     user1 = User.objects.filter(email=request.POST['email'])
    #     if user1.exists():
    #         messages.error(
    #             request, "This email is already Registered!", extra_tags='register')
    #         return redirect('/')

    #     if len(errors) > 0:
    #         for key, value in errors.items():
    #             messages.error(request, value, extra_tags=key)
    #         return redirect('/')
    #     else:
    #         user1 = User.objects.create(
    #             first_name=request.POST['first_name'],
    #             last_name=request.POST['last_name'],
    #             email=request.POST['email'],
    #             password=bcrypt.hashpw(
    #                 request.POST['password'].encode(), bcrypt.gensalt()).decode()
    #         )
    #         request.session['log_user_id'] = user1.id
    #     return redirect('/')

    # return redirect("/")
# login


def add_item(request):
    return render(request, template_name='add_item.html')


def create(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user1 = User.objects.last()
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
