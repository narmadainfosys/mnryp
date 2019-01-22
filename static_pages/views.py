from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'static_pages/about.html')
def home(request):
    return render(request, 'static_pages/home.html')

