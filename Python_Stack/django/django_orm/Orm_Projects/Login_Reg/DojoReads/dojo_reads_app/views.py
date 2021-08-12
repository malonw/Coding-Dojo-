from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Reviews
import bcrypt

# log in and registration


def index(request):

    return render(request, 'index.html')

# registration


def register(request):
    if request.method == "GET":
        return redirect("/landing.html")
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
        return redirect('/home')

    return redirect("/")
# login


def login(request):
    user_list = User.objects.filter(email=request.POST['email'])
    if user_list:
        logged_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['log_user_id'] = logged_user.id

            return redirect('/home')
        else:
            messages.error(request, "Invalid email or password.",
                           extra_tags='login')
            return redirect('/')
    messages.error(request, "Email does not exist.", extra_tags='login')
    return redirect('/')

# logout


def logout(request):
    request.session.clear()
    return redirect('/')

# home view Recent Book Reviews, Other books with Reviews


def home(request):

    context = {
        'user': User.objects.get(id=request.session['log_user_id']),
        'user_books': Book.objects.all(),
    }
    # this_book = Book.objects.last()
    # this_book.review.filter(id=user).exists():

    return render(request, 'home.html', context)


def add_book(request):
    context = {
        'authors': Book.objects.all()

    }
    return render(request, 'new_book_review.html', context)


def new_book(request):
    if request.method == 'POST':
        errors1 = Book.objects.book_validator(request.POST)
    if len(errors1) > 0:
        for key, value in errors1.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/add_book')

    else:

        user = request.session['log_user_id']
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],

        )
        Reviews.objects.create(
            review=request.POST['review'],
            rating=request.POST['rating'],
        )

    return redirect('/home')


def book_details_review(request, book_id):
    context = {
        'user': User.objects.get(id=request.session['log_user_id']),
        'user_books': Book.objects.all(),
        'books': Book.objects.get(id=book_id),
    }

    return render(request, 'book_review.html', context)


def user_info(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
        'books_reviewed': Book.objects.filter(id=user_id),
    }

    # add page to see user name, email and number of reviews and books reviewed
    return render(request, 'user_info.html', context)


def update_review(request, book_id):
    # add method to update a book review
    return redirect('/book_details_review')


def destroy(request, book_id):

    # add method to delete a book review if owned
    return redirect('/book_details_review')
