from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

# Create your views here.

def index(request):
    restaurants = Restaurant.objects.order_by('ville')
    return render(request, 'restaurant/index.html', {'list_restaurants' : restaurants})


