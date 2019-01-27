from django.shortcuts import render, get_object_or_404
from .models import Category, Listing
from .forms import ListingForm
# Create your views here.

def categories(request):
    template = 'categories/categories.html'

    categories = Category.objects

    context = {
        'categories':categories,
    }
    return render(request, template, context)

def listings(request):
    template = 'categories/listings.html'

    listings = Listing.objects

    context = {
        'listings':listings,
    }
    return render(request, template, context)

def category(request, slug):
    template = 'categories/category.html'

    category = get_object_or_404(Category, slug=slug)
    listings = Listing.objects.filter(category = category)

    context = {
        'category':category,
        'listings':listings,
    }
    return render(request, template, context)

def listing(request, slug):
    template = 'categories/listing.html'
    print(slug)

    listing = Listing.objects.filter(slug = slug)
    print(listing)

    context = {
        'listing':listing,
    }
    return render(request, template, context)

def create_listing(request):
    template = 'categories/create_listing.html'

    form = ListingForm()

    context = {
        'form':form
    }
    return render(request, template, context)
