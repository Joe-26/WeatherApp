from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import WorldCities
import requests
import geocoder
from datetime import datetime
import random

# Create your views here.
def get_temp(location):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m&temperature_unit=fahrenheit"
    response = requests.get(api_request).json()

    now = datetime.now()
    hour = now.hour

    currTemp = response['hourly']['temperature_2m'][hour]

    return currTemp

def temp_here(request):
    location = geocoder.ip('me').latlng

    template = loader.get_template('index.html')
    context = {'city':'your Location','temp': get_temp(location)}
    return HttpResponse(template.render(context, request))

def temp_other(request):
    cities = WorldCities.objects.all()
    city = random.choice(cities)
    location = [city.lat, city.lng]

    template = loader.get_template('index.html')
    context = {'city':city.city, 'country':city.country, 'temp': get_temp(location)}
    return HttpResponse(template.render(context, request))

def add_city(request):
    return render(request, 'addCity.html')