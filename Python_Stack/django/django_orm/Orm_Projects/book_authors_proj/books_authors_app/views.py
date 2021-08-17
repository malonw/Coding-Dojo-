from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author


def index(request):
    context = {
        'all_books': Book.objects.all()
    }

    return render(request, "index.html", context)


def add_book(request):
    if request.method == 'POST':
        errors1 = Book.objects.book_validator(request.POST)
    if len(errors1) > 0:
        for key, value in errors1.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')

    else:
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],

        )
    return redirect('/')


def view_book(request, id):
    view_book_query = {
        'book': Book.objects.get(id=id),
        'all_authors': Author.objects.all()
    }
    return render(request, 'view_one_book.html', view_book_query)


def authors_index(request):
    author_query = {
        'all_authors': Author.objects.all()
    }
    return render(request, "authors.html", author_query)


def add_author(request):
    if request.method == 'POST':
        errors = Author.objects.author_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/authors')

    else:
        Author.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            notes=request.POST['desc'],
        )
    return redirect('/authors')

def add_author_to_book(request, book_id):
    this_book = Book.objects.get(id=book_id)
    if request.method == "POST":
        this_book.book_authors.filter(id=book_id)
    


def view_author(request, id):
    view_author_query = {
        'author': Author.objects.get(id=id),
        'books': Book.book_authors.through.objects.filter(id=id),

    }
    return render(request, 'view_one_author.html', view_author_query)


# Create your views here.
