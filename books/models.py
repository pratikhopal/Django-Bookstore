from django.db import models
from django.db.models.base import Model

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=256)
    pageCount=models.IntegerField(default=0)
    thumbnailUrl=models.CharField(max_length=256,null=True)
    shortDescription=models.CharField(max_length=256,null=True)
    longDescription=models.TextField(null=True)

def __str__(self):
    return self.title


class Review(models.Model):
    body=models.TextField(null=True)
    book=models.ForeignKey(book,on_delete=models.CASCADE,null=True)