from django.shortcuts import render
from requests import request
# Create your views here.

def home_view(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = request.get(url).json()