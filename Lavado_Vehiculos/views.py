from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicios
from .form import Agendar_HoraForm
from Lavado_Vehiculos.models import Agendar_Hora

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

def Agregar_Hora(request):

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
        agendar_hora = Agendar_Hora.objects.all()
        data = {
            'agendar_hora': agendar_hora
        }
        return render(request,'Admin/Listar.html', data)
    
def Modificar(request, id):   
        agendar_hora = get_object_or_404(Agendar_Hora, id=id)
        data = {
            'form' : Agendar_HoraForm(instance=agendar_hora)
        }
        if request.method == 'POST':
            formulario = Agendar_HoraForm(data=request.POST, instance=agendar_hora, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="Listar")
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"
        return render(request, "Admin/Modificar.html", data)
                
def Eliminar(request, id):   
        agendar_hora = get_object_or_404(Agendar_Hora, id=id)
        agendar_hora.delete()
        return redirect(to="Listar")