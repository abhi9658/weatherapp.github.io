from multiprocessing import context
import re
from django.shortcuts import render
import requests
from .models import City
from .forms  import CityForm


def index(request):
      api_key = "46e885e0cdfe3f55b9c67867cfff6ac6"
      if request.method == "POST":
          form = CityForm(request.POST)
          form.save()
      form = CityForm()
      
      weather_data = []
      cities = City.objects.all()
      for city in cities:
          url = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+str(city)
          city_weather = requests.get(url).json() 
          weather = {
              'city' : city_weather['name'],
              'temperature' : city_weather['main']['temp'],
              'description' : city_weather['weather'][0]['description'],
              'icon' : city_weather['weather'][0]['icon']
          }
          weather_data.append(weather)
      context = {'weather_data':weather_data, 'form' : form}
      return render(request, 'weather/index.html', context, ) 

