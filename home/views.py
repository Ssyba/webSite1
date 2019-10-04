import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def current_city_name():
    my_ip = requests.get('https://api.myip.com').json()
    payload = requests.get('http://ip-api.com/json/' + my_ip['ip']).json()
    return payload['city']


@csrf_exempt
def home(request):
    token = '2f43c98b5a78c9dcff0740521379af44'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + token

    def city_info(cit):
        re = requests.get(url.format(cit)).json()
        city_weather = {
            'city': cit.name if hasattr(cit, 'name') else cit,
            'temperature': re['main']['temp'],
            'description': re['weather'][0]['description'],
            'icon': re['weather'][0]['icon'],
        }
        return city_weather

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                    messages.success(request, 'City added successfully!')
                elif r['cod'] == '404':
                    messages.error(request, 'Not a real city!')
                else:
                    messages.error(request, 'Something went wrong with the request to OpeanWeather')
            else:
                messages.error(request, 'City is already in the DB!')
        return redirect('home')

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        weather_data.append(city_info(city))

    context = {'city_weather': city_info(current_city_name()),
               'weather_data': weather_data,
               'form': form}
    return render(request, 'home/home.html', context)


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    messages.info(request, '"{}" was deleted from "Added Cities Weather"'.format(city_name))
    return redirect('/')
