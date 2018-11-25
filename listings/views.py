from django.shortcuts import render,get_object_or_404
from .models import Listing

from .choices import bedroom_choices,price_choices,state_choices

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'listings':page_listings,
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    data = {
        'listing':listing
    }
    return render(request,'listings/listing.html',data)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        keywords = request.GET['city']
        if keywords:
            queryset_list = queryset_list.filter(city__iexact=city)

    data = {
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'listings':queryset_list
    }

    return render(request,'listings/search.html',data)
