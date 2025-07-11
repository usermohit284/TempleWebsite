from django.urls import path
from .views import home  
from .views import services_view
from .views import puja_view

urlpatterns = [
    path('', home, name='home'), 
    path('services/', services_view, name='services'),
    path('puja/', puja_view, name='puja'),

]


