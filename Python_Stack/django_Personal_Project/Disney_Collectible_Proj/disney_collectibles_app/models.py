from django.db import models
from django.db.models.fields import CharField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

# User Login and Registration
# class UserManager(models.Manager):
#     def user_validator(self, postData):
#         errors = {}
#         EMAIL_REGEX = re.compile(
#             r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#         if len(postData['fname']) < 2:
#             errors['fname'] = "First name must be 2 characters or more."
#         if len(postData['lname']) < 2:
#             errors['lname'] = "Last name must be 2 characters or more."
#         if not EMAIL_REGEX.match(postData['email']):
#             errors['email'] = "Invalid email address!"

#         if len(postData["password"]) < 8:
#             errors['password'] = "Password must be at least 8 characters."
#         if postData['password'] != postData['password2']:
#             errors['password'] = "Passwords do not match"
#         return errors

#     def login_validator(self, postData):
#         errors = {}
#         EMAIL_REGEX = re.compile(
#             r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#         if not EMAIL_REGEX.match(postData['email']):
#             errors['email'] = "Invalid email address!"
#         if len(postData["password"]) < 8:
#             errors['password'] = "Password must be at least 8 characters."
#         return errors
def validaeLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )

def email_validation(value):
    validator = RegexValidator( r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$' )
    validator(value)
    return value



class User(models.Model):
    fname = models.CharField(max_length=100, validators=[validaeLengthGreaterThanTwo])
    lname = models.CharField(max_length=100, validators=[validaeLengthGreaterThanTwo])
    email = models.EmailField(max_length=100, validators=[email_validation])
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = UserManager()


class Catagory(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class ItemManager(models.ManyToManyRel):
    def item_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors['name'] = "Name Required."
        if len(postData['catagory']) < 2:
            errors['catagory'] = "Catagory must be 2 characters or more."
        if len(postData['desc']) < 2:
            errors['desc'] = "Description must be 2 characters or more."
        if len(postData['value']) < 1:
            errors['value'] = "Value Required."
        if len(postData['manufacturer']) < 2:
            errors['manufacturer'] = "Manufacturer must be 2 characters or more."


class Item(models.Model):
    name = models.CharField(max_length=255)
    catagory = models.ManyToManyField(Catagory, related_name='catagories')
    desc = models.TextField()
    quantity = models.IntegerField()
    condition = models.BooleanField(default=True)
    value = models.IntegerField()
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="maker", on_delete=models.CASCADE)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
