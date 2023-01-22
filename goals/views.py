from django.shortcuts import render


# Create your views here.
def goals(request):
    return render(request, 'goals.html')
    

