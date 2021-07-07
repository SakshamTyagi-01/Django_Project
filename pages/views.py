from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices


def index(response):
    listings = Listing.objects.order_by('-list_date').filter(is_publish=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices':price_choices
    }
    return render(response,'pages/index.html',context)

def about(response):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get Mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(response,'pages/about.html',context)