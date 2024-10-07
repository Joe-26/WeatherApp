from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import WorldCities
import requests
import geocoder
from datetime import datetime
import random

# Create your views here.
def temp_here(request):
    location = geocoder.ip('me').latlng
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m&temperature_unit=fahrenheit"
    response = requests.get(api_request).json()
    
    now = datetime.now()
    hour = now.hour

    currTemp = response['hourly']['temperature_2m'][hour]

    template = loader.get_template('index.html')
    context = {'city':'your Location','temp': currTemp}
    return HttpResponse(template.render(context, request))

def temp_other(request):
    cities = WorldCities.objects.all()

    location = random.choice(cities)
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location.lat}&longitude={location.lng}&hourly=temperature_2m&temperature_unit=fahrenheit"
    response = requests.get(api_request).json()

    now = datetime.now()
    hour = now.hour

    currTemp = response['hourly']['temperature_2m'][hour]

    template = loader.get_template('index.html')
    context = {'city':location.city, 'temp': currTemp}
    return HttpResponse(template.render(context, request))