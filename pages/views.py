from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.
def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)[:3]
    print("this is the index page")
    context = {
        'listings': listings
    }
    return render(request, "pages/index.html", context)

def about(request):
    #Gel all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #Get Mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, "pages/about.html", context)