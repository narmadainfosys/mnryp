from django.shortcuts import render, get_object_or_404
from .models import Category, Listing
# Create your views here.
def categories(request):
    categories = Category.objects
    return render(request, 'categories/categories.html', {'categories':categories})
def listings(request):
    listings = Listing.objects
    return render(request, 'categories/listings.html', {'listings':listings})

def category(request, slug):
    template = 'categories/category.html'

    category = get_object_or_404(Category, slug=slug)
    post = Listing.objects.filter(category = category)

    context = {
        'category':category,
        'post':post,
    }
    return render(request, template, context)
