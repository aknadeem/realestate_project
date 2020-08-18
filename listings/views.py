from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

# Create your views here.

def index(request):
	listings = Listing.objects.all()

	paginator = Paginator(listings, 6)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)	

	context = { 
		'listings' : paged_listings 
	}

	return render(request, 'listing/listings.html', context)

def listing(request, listing_id):
	return render(request, 'listing/listing.html')

def search(request):
	# return HttpResponse('search')
	return render(request, 'listing/search.html')
