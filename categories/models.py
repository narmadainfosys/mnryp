from django.db import models
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=150)
    slug = AutoSlugField(max_length=50, unique=True, populate_from='name')

    created_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

class Listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=200)
    full_description = models.CharField(max_length=1000)
    contact_person = models.CharField(max_length=50)
    business_address = models.CharField(max_length=50)
    email_address = models.EmailField(blank=True)
    business_fax = PhoneNumberField(blank=True)
    phone_number = PhoneNumberField()
    phone_number_second = PhoneNumberField(blank=True)
    zip_code = models.PositiveIntegerField(blank=True)
    country = CountryField(default='NP')
    slug = AutoSlugField(max_length=150, unique=True, populate_from='title')

    created_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

