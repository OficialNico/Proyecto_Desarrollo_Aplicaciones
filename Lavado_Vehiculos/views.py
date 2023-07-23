from django.shortcuts import render, redirect
from .models import Servicios, Agendar_Hora
from .form import Agendar_HoraForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

from .models import CustomUser
# Create your views here.

def Home(request):
    servicios =Servicios.objects.order_by('-id')[:6]
    Datos ={
        "Servicios":servicios,
    }
    return render(request, "Home/Home.html", Datos)

def Agendar_Hora(request):

        data = {
        'form' :Agendar_HoraForm(),
        }

        if request.method == 'POST':
            formulario = Agendar_HoraForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "guardado correctamente"
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"

        return render(request, "Servicios/Agendar_Hora.html", data)

def Listar(request):
        agendar_hora = Agendar_Hora.objects.order_by('-id')[:1]
        data = {
         'agendar_hora': agendar_hora
         }
        return render(request,'Admin/Listar.html', data)