from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
