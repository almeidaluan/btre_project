from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

from listings.choices import price_choices,bedroom_choices,state_choices

def home(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    data = {
        'listings':listings,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices': state_choices,
    }

    return render(request,'pages/index.html',data)

def about(request):
    
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    data = {
        'realtors': realtors,
        'mvp_realtors':mvp_realtors,
    }

    return render(request,'pages/about.html',data)

