from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.

def home_view(requests):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    
    context = {'data':data}
    return render(requests, 'postions/main.html',context)