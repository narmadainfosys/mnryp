from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
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

    listing = Listing.objects.filter(slug = slug)

    context = {
        'listing':listing,
    }
    return render(request, template, context)

def create_listing(request):
    template = 'categories/create_listing.html'

    if request.method == "POST":
        listing_form = ListingForm(request.POST)
        if listing_form.is_valid():
            listing_form.save()
            return redirect('listings')

    else:
        listing_form = ListingForm()

    context = {
        'form':listing_form,
    }
    return render(request, template, context)

def edit_listing(request, slug):
    template = 'categories/edit_listing.html'

    listing = get_object_or_404(Listing, slug=slug)

    if request.method == "POST":
        edit_form = ListingForm(request.POST, instance=listing)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('listings')
    else:
        edit_form = ListingForm(instance=listing)

    context = {
        'form':edit_form,

    }
    return render(request, template, context)

def delete_listing(request, slug):
    template = 'categories/delete_listing.html'

    listing = get_object_or_404(Listing, slug=slug)

    if request.method == "POST":
        listing.delete()
        return redirect('listings')

    context = {
        'listing':listing,
    }
    return render(request, template, context)





def search(request):
    template = 'categories/listings.html'

    query = request.GET.get('q')

    results = Listing.objects.filter(Q(title__icontains=query) | Q(full_description__icontains=query) | Q(short_description__icontains=query))

    context = {
        'items': results,
    }
    return render(request, template, context)
