
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Make sure 'index.html' is inside templates

from django.shortcuts import render

def services_view(request):
    return render(request, 'services.html')
