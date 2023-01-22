from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import requests
import json


def weather_api(request):
    """
    A view to handle weather api calls
    """
    if request.method == "GET":
        return HttpResponse(content="Weather Test Api Route", status=200)
    return HttpResponse(status=400)


def converter_api(request):
    """
    A view to handle exchange rate api currency conversion
    """
    if request.method == "GET":
        return HttpResponse(content="Converter Test Api Route", status=200)
    return HttpResponse(status=400)


def get_currencies(request):
    """
    A view to get a list of currencies.
    """
    url = "https://api.apilayer.com/exchangerates_data/symbols"

    payload = {}
    headers = {
        "apikey": settings.EXCHANGE_API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    data = json.loads(response.text)

    return JsonResponse(data)
