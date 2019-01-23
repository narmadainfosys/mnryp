from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=150)

class Listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    full_description = models.CharField(max_length=1000)


