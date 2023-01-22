from django.shortcuts import render
from django.http import HttpResponse


def weather_api(request):
    """
    A view to handle weather api calls
    """
    if request.method == "POST":
        return HttpResponse(content="Weather Test Api Route", status=200)
    return HttpResponse(status=400)


def converter_api(request):
    """
    A view to handle weather api calls
    """
    if request.method == "POST":
        return HttpResponse(content="Converter Test Api Route", status=200)
    return HttpResponse(status=400)
