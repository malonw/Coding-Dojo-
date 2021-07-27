from django.db import models
from django.db.models.fields import DateTimeField

class users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email_address=models.EmailField(max_length=255)
    age=models.IntegerField(default=0)
    created_at=DateTimeField(auto_now_add=(True))
    updated_at=DateTimeField(auto_now=True)
    def __repr__(self):
        
        return f"({self.id}){self.first_name}{self.last_name}{self.age} "
        

# Create your models here.
