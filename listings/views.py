from django.shortcuts import render
from .models import Listing

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    
    listings = Listing.objects.all()

    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'listings':page_listings,
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    #listing = Listing.objects.get(id=listing_id)
    return render(request,'listings/listing.html')

def search(request):
    return render(request,'listings/search.html')
