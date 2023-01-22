from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests
import json


def weather_api(request):
    """
    A view to handle weather api calls
    """
    if request.method == "GET":
        return HttpResponse(content="Weather Test Api Route", status=200)
    return HttpResponse(status=400)


@csrf_exempt
def converter_api(request):
    """
    A view to handle exchange rate api currency conversion
    """
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    from_query = body['from_query']
    to_query = body['to_query']
    amount_query = body['amount_query']

    url = ("https://api.apilayer.com/exchangerates_data/convert?"
           f"to={to_query}&from={from_query}&amount={amount_query}")

    payload = {}
    headers = {
        "apikey": settings.EXCHANGE_API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    data = json.loads(response.text)
    return JsonResponse(data)


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
