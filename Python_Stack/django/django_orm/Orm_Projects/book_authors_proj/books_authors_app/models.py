from django.db import models

class AuthorManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "First name must be more than 2 characters."
        if len(postData['lname']) < 2:
            errors['lname'] = "Last name must be more than 2 characters."

class Author(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors1 = {}
        if len(postData['title']) < 1:
            errors1['title'] = "Title must be more than 1 character."
        if len(postData['desc']) < 5:
            errors1 = "Description must be more than 5 characters."
            

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    book_authors = models.ManyToManyField(Author, related_name="books_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()


# Create your models here.
