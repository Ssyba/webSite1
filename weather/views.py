import requests
from django.shortcuts import render

def get_ip():
    ip = requests.get('https://api.myip.com').json()
    return ip['ip']

def get_my_city():
    payload = requests.get('http://ip-api.com/json/'+get_ip()).json()
    return payload['city']

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=2f43c98b5a78c9dcff0740521379af44'
    city = get_my_city()

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}
    print(get_my_city())
    return render(request, 'weather/weather.html', context)
