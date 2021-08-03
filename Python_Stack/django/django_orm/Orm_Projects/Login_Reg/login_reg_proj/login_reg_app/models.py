from typing_extensions import Required
from django.db import models
from django.db.models.fields import EmailField
from django.forms.widgets import PasswordInput

class NewUser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(Required=True)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
