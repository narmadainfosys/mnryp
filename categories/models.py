from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=150)

class Listing(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    full_description = models.CharField(max_length=1000)


