from django.urls import path
from .views import home  
from .views import services_view

urlpatterns = [
    path('', home, name='home'), 
    path('services/', services_view, name='services'),
]


