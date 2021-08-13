from django.db import models
import re

from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['fname']) < 2:
            errors['fname'] = "First name must be 2 characters or more."
        if len(postData['lname']) < 2:
            errors['lname'] = "Last name must be 2 characters or more."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData["password"]) < 8:
            errors['password'] = "Password must be at least 8 characters."
        if postData['password'] != postData['password2']:
            errors['password'] = "Passwords do not match"
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData["password"]) < 8:
            errors['password'] = "Password must be at least 8 characters."
        return errors


class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


class BookManager(models.Manager):
    def book_validator(self, postData):
        errors1 = {}
        if len(postData['title']) <= 0:
            errors1['title'] = "Title Required."
        # if len(postData['review']) < 5:
        #     errors1['review'] = "Review must be more than 5 characters."
        return errors1


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    a_review = models.ManyToManyField(User, related_name="user_reviews")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BookManager()


class Reviews(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user_review = models.ForeignKey(
        User, related_name='user_reviewed', on_delete=models.CASCADE)
    book_review = models.ForeignKey(
        Book, related_name='book_reviewed', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
