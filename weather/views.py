import requests
from django.shortcuts import render
from weather.models import City
from.forms import CityForm


def index(request):
    appid='d54c5ba496240d30fc181cd162b7738c'
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form=CityForm()

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'wind': res["wind"]["speed"]
        }
        all_cities.append(city_info)

    context={'all_info': all_cities,'form':form}

    return render(request,'weather/index.html',context)
