from django.db import models
import re


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


class Catagory(models.Model):
    cname = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Manufacturer(models.Model):
    mname = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class ItemManager(models.ManyToManyRel):
    def item_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors['name'] = "Name Required."
        if len(postData['prod_cat']) < 2:
            errors['prod_cat'] = "Catagory must be 2 characters or more."
        if len(postData['desc']) < 2:
            errors['desc'] = "Description must be 2 characters or more."
        if len(postData['value']) < 1:
            errors['value'] = "Value Required."
        if len(postData['prod_man']) < 2:
            errors['prod_man'] = "Manufacturer must be 2 characters or more."


class Item(models.Model):
    name = models.CharField(max_length=255)
    prod_cat = models.ManyToManyField(Catagory, related_name='catagories')
    desc = models.TextField()
    quantity = models.IntegerField()
    condition = models.CharField(max_length=20)
    value = models.IntegerField()
    prod_man = models.ForeignKey(
        Manufacturer, related_name="maker", on_delete=models.CASCADE)
    image = models.ImageField()
    favorite = models.ManyToManyField(
        User, related_name="my_fav")

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
