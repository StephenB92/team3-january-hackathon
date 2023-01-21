from django.urls import path
from . import views

urlpatterns = [
    path('', views.cahsbook, name='cashbook'),
    
]