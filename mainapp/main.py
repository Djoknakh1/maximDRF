import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'drf.settings'
django.setup()

import requests, pprint

from mainapp.models import Vacancy

response = requests.get('https://api.hh.ru/vacancies')
response = response.json()

for i in range(10):
    response = requests.get(f'https://api.hh.ru/vacancies/?page={i}').json()
    for vacancy in response:
        Vacancy(**vacancy)
# pprint.pprint(response)