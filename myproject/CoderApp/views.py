from ast import Import
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from CoderApp.models import Mascota
import datetime


def mascotas(request):
    mascota1= Mascota(nombre="Chiquita", parentesco="Perrita de mi novio, Rodri.", edad=7, cumpleanios=datetime.datetime(2015, 3, 20))

    mascota1.save()
    mascota2= Mascota(nombre="Juana", parentesco="Mi hija", edad=4, cumpleanios=datetime.datetime(2018, 12, 23))
    mascota2.save()
    mascota3= Mascota(nombre="Cleto", parentesco="Sobrino", edad=10, cumpleanios=datetime.datetime(2012, 2, 26))
    mascota3.save()
    lista=[mascota1, mascota2, mascota3]

    return render(request, "mascotas.html", {"listita" : lista})