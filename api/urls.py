from django.urls import path
from . import views

urlpatterns = [
    path("weather/", views.weather_api),
    path("convert/", views.converter_api),
    path("get_currencies/", views.get_currencies),
]
