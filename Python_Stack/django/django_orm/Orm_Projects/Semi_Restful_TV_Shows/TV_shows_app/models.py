from django.db import models
from django.db.models.functions import Now
from datetime import date
from django.core.validators import MaxLengthValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be more than 2 characters."
        if len(postData['network']) < 3:
            errors["network"] = "Network should be more than 3 characters."
        if len(postData['descript']) < 10 or len(postData['descript']) > 0:
            errors["descript"] = "Description should be more than 10 characters."
        # if postData['release_date'] > date.today:
        #     errors["release_date"] = "Release date cannot be in the Future!"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    # release_date = models.DateField(
    #     validators=[MaxValueValidator(limit_value=date.today)])
    descript = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"({self.id}){self.title}{self.network}{self.release_date}{self.descript} "

    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             check=models.Q(release_date__lte=Now()),
    #             name='release_date_cannot_be_in_future_dated'
    #         )
    #     ]
# Create your models here.
