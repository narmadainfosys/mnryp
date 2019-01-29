from django.shortcuts import render
from search.documents import ListingDocument

# Create your views here.

def search(request):
    template = 'search/search.html'

    q = request.GET.get('q')

    if q:
        listings = ListingDocument.search().query("match", title=q)
    else:
        print("no q-------------------------")
        listings = ''

    context={
        'listings': listings
    }

    print(type(listings))
    print(listings)

    return render(request, template, context)
