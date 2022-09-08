from django.urls import path

from .views import *






urlpatterns = [
path("", mascotas, name= "mascotas"),
    
]