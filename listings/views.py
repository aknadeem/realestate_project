from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing

# Create your views here.

def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)

	paginator = Paginator(listings, 6)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)	

	context = { 
		'listings' : paged_listings 
	}

	return render(request, 'listing/listings.html', context)

def listing(request, listing_id):
	listing = get_object_or_404(Listing, pk=listing_id)

	context = {
		'listing': listing
	}
	
	return render(request, 'listing/listing.html', context)

def search(request):
	# return HttpResponse('search')

	listings = Listing.objects.order_by('-list_date')

	#keywords Search
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			listings = listings.filter(description__icontains=keywords)

	#City Search
	if 'city' in request.GET:
		city = request.GET['city']
		if city:
			listings = listings.filter(city__iexact=city)

	#State Search
	if 'state' in request.GET:
		state = request.GET['state']
		if state:
			listings = listings.filter(state__iexact=state)

	#Bedrooms Search
	if 'bedrooms' in request.GET:
		bedrooms = request.GET['bedrooms']
		if bedrooms:
			listings = listings.filter(bedrooms__lte=bedrooms)

	#Price Search
	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			listings = listings.filter(price__lte=price)

	context = { 
		'listings' : listings,
		'price_choices' : price_choices,
		'bedroom_choices' : bedroom_choices,
		'state_choices' : state_choices,
		'values' : request.GET
	}

	return render(request, 'listing/search.html', context)
