from django.db import models
from django.db.models.fields import DateTimeField

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(auto_now=True)
    descript = models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"({self.id}){self.title}{self.network}{self.release_date}{self.descript} "

# Create your models here.
