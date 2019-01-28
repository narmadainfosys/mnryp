from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=150)
    slug = AutoSlugField(max_length=50, unique=True, populate_from='name')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

class Listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=200)
    full_description = models.CharField(max_length=1000)
    slug = AutoSlugField(max_length=150, unique=True, populate_from='title')

    def __str__(self):
        return self.title

