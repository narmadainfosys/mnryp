from django.shortcuts import render
from .models import Category, Listing
# Create your views here.
def categories(request):
    categories = Category.objects
    return render(request, 'categories/categories.html', {'categories':categories})
def listings(request):
    listings = Listing.objects
    return render(request, 'categories/listings.html', {'listings':listings})

