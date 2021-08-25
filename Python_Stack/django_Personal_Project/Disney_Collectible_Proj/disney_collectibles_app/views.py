from django.shortcuts import render, redirect
from django.contrib import messages  # import messages
from .models import User, Item, Manufacturer, Catagory
import bcrypt


def homepage(request):
    context = {
        'user': User.objects.get(id=request.session['log_user_id'])
    }
    return render(request, 'main/home.html', context)


# log in and registration
def index(request):
    return render(request, 'main/index.html')

# registration
def register(request):

    return render(request, 'main/register.html')


def register_request(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        user1 = User.objects.filter(email=request.POST['email'])
        if user1.exists():
            messages.error(
                request, "This email is already Registered!", extra_tags='register')
            return redirect('/main/login')

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/main/register')
        else:
            user1 = User.objects.create(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                email=request.POST['email'],
                password=bcrypt.hashpw(
                    request.POST['password'].encode(), bcrypt.gensalt()).decode()
            )
            request.session['log_user_id'] = user1

        return redirect('/main/home')

    return redirect("/")
# login


def login(request):
    return render(request, 'main/login.html')


def login_request(request):
    user_list = User.objects.filter(email=request.POST['email'])
    if user_list:
        logged_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['log_user_id'] = logged_user.id
            return redirect('/main/home')
        else:
            messages.error(request, "Invalid email or password.",
                           extra_tags='login')
            return redirect('/main/login')
    messages.error(request, "Email does not exist.", extra_tags='login')
    return redirect('/main/login')

# logout


def logout_request(request):
    request.session.clear()
    return redirect('/')


def add_item(request):
    return render(request, 'add_item.html')


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
