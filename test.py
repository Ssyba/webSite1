import requests
import socket
from django.shortcuts import render

def get_ip():
    ip = requests.get('https://api.myip.com').json()
    return ip['ip']

def get_my_city():
    payload = requests.get('http://ip-api.com/json/'+get_ip()).json()
    return payload['city']


print(get_my_city())
