from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza

# Create your views here.

# EXERCICE
# LES PIZZAS :BOLOGNAISE : 13,79 €, NOËL : 22,65 €, VIZZA : 12,55 €,
# PRINTANIERE : 11,90 €, PATATOR : 14,85 €

def index(request):

    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas' : pizzas})

def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json= serializers.serialize("json", pizzas)
    return HttpResponse(json)