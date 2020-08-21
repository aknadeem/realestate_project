from django.shortcuts import render, redirect
from django.contrib import messages, auth

from django.contrib.auth.models import User

# from listings.choices import price_choices, bedroom_choices, state_choices
# from listings.models import Listing
# from realtors.models import Realtor

# Create your views here.

def login(request):
	if request.method == 'POST':
		username  = request.POST['username']
		password  = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			messages.success(request, 'You are loggedin Successfully')
			return redirect('dashboard')
		else:
			messages.error(request, 'Invalid username or password')
			return redirect('login')
	else:		
		return render(request, 'accounts/login.html')

def register(request):
	if request.method == 'POST':

		# Get form values
		first_name  = request.POST['first_name']
		last_name  = request.POST['last_name']
		username  = request.POST['username']
		email  = request.POST['email']
		password  = request.POST['password']
		password2  = request.POST['password2']

		# check if password match
		if password == password2:
			# checkk username if exists
			if User.objects.filter(username=username).exists():
				messages.error(request, 'That username is taken')
				return redirect('register')
			else:
				# checkk Email if exists
				if User.objects.filter(email=email).exists():
					messages.error(request, 'That Email is being Used')
					return redirect('register')
				else:
					# Create User
					user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
					# Login after Register
					# auth.login(request, user)
					# messages.success(request, 'You are Now Logged in')
					# return redirect('index')
					user.save()
					messages.success(request, 'You are Now Register and can login')
					return redirect('login')
		else:
			messages.error(request, 'Password don’t match')
			return redirect('register')
	else:		
		return render(request, 'accounts/register.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request, 'You are Now Logout')
		return redirect('index')

	return redirect('index')

def dashboard(request):
	# return HttpResponse('dashboard')

	# context = { 
	# 	'listings' : listings,
	# 	'price_choices' : price_choices,
	# 	'bedroom_choices' : bedroom_choices,
	# 	'state_choices' : state_choices
	# }
	# return render(request, 'pages/index.html', context)
	return render(request, 'accounts/dashboard.html')
