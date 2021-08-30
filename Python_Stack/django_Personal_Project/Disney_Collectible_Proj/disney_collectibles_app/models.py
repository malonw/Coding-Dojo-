from django.db import models
from django.contrib.auth.models import User






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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
