from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def homeImage(request):

	return render_to_response('home/base.html')

def about(request):

	return render_to_response('home/about.html')

def contact(request):

	return render_to_response('home/contact.html')	