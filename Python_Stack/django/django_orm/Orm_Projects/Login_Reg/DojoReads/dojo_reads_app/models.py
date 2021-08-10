from login_reg_app.models import User
from django.db import models




class BookManager(models.Manager):
    def book_validator(self, postData):
        errors1 = {}
        if len(postData['title']) <= 0:
            errors1['title'] = "Title Required."
        if len(postData['desc']) < 5:
            errors1['desc'] = "Decription must be more than 5 characters."
        return errors1


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    reviewed_by = models.ForeignKey(User, related_name="book_review_by", on_delete=models.CASCADE,)
    review = models.ManyToManyField(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BookManager()




# Create your models here.
