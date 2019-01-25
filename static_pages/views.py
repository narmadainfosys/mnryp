from django.shortcuts import render

# Create your views here.

def about(request):
    template = 'static_pages/about.html'

    return render(request, template)

def home(request):
    template = 'static_pages/home.html'

    return render(request, template)

def contact(request):
    template = 'static_pages/contact.html'

    return render(request, template)

def privacy_policy(request):
    template = 'static_pages/privacy_policy.html'

    return render(request, template)
