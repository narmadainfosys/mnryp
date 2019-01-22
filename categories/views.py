from django.shortcuts import render

# Create your views here.
def categories(request):
    return render(request, 'categories/categories.html')
def listings(request):
    return render(request, 'categories/listings.html')

