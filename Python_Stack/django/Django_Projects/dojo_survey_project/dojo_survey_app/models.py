from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=255)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

class Favorite_Dojo(models.Model):
    pass
# Create your models here.
