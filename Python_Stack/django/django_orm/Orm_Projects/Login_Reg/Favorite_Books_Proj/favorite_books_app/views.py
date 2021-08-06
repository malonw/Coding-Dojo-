from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, User
import bcrypt

    # log in and registration 

def landing(request):
    return render(request, 'landing.html')


def register(request):
    if request.method == "GET":
        return redirect("/landing.html")
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        user1 = User.objects.filter(email=request.POST['email'])
        if user1.exists():
            messages.error(request, "You have already Registered!")
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
# login

def login(request):
    user_list = User.objects.filter(email=request.POST['email'])
    if user_list:
        logged_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['log_user_id'] = logged_user.id
            return redirect('/redirect_view')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('/')
    messages.error(request, "Email does not exist.")
    return redirect('/')

# logout
def logout(request):
    request.session.clear()
    return redirect('/')

# Redirect view
def redirect_view(request):
    response = redirect('/redirect-success')
    return response

# Success Page/ User View 
def books(request):
    errors = Book.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('redirect_view')

    context = {
        'user': User.objects.get(id=request.session['log_user_id']),
        'user_books': Book.objects.all(),
        # 'fav_books': Book.objects.get(id=id),
    }
    return render(request, 'books.html', context)

def add_book(request):
    if request.method == 'POST':
        errors = Book.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('redirect_view')

        else:

            Book.objects.create(
                title=request.POST['title'],
                desc=request.POST['desc'],
            )
            messages.success(request, 'Book Created')
            # Show.objects.last()
        return redirect('redirect_view')






    #Edit query 

def edit(request, id):
    # if request.session['id'] == 

    edit_query = {
        'books': Book.objects.get(id=id)
    }
    return render(request, 'book_detail.html', edit_query)


# to update a Book Description

def update(request, id):
    if request.method == 'POST':
        errors = Book.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/" + id + '/edit')
        else:
            update = Book.objects.get(id=id)
            update.title = request.POST['title']
            update.desc = request.POST['desc']
            update.save()
            messages.success(request, 'Book Description Updated')
        return redirect('/')


# to Delete a book

def destroy(request, id):
    if request.method == "POST":
        messages.warning(request, "Are you sure you want to delete this book :{books.title}?")
        dele = Book.objects.get(id=id)
        dele.delete()
    return redirect('/books')




