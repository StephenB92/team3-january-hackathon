from django.urls import path
from . import views

urlpatterns = [
    path('', views.goals, name='goals'),
    
]