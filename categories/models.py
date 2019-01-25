from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

class Listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    full_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

