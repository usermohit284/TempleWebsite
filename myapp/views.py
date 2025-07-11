
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  

from django.shortcuts import render

def services_view(request):
    return render(request, 'services.html')

from django.shortcuts import render

def puja_view(request):
    return render(request, 'puja.html') 

def puja_details(request):
    return render(request, 'puja-details.html')  




