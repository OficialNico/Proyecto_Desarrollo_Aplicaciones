from django.shortcuts import render
from.models import Servicios, Agendar_Hora

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

from .models import CustomUser
# Create your views here.

def Home(request):
    Servicios =Servicios.objects.order_by('-id')[:6]
    Datos ={
        "Servicios":Servicios,
    }
    return render(request, "TemplatesHtml/Home.html", Datos)


def Agendar_Hora(request):
    TomarDatos = Agendar_Hora.objects.all()
    Datos = { "DatosTablaAgendar_Hora":TomarDatos }
    return render(request, "TemplatesHtml/Agendar_Hora.html", Datos)



