from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'listing/listings.html')

def listing(request):
	return render(request, 'listing/listing.html')

def search(request):
	# return HttpResponse('search')
	return render(request, 'listing/search.html')
