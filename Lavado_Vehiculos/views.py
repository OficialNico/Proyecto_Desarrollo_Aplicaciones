from django.shortcuts import render, redirect
from.models import Servicios, Agendar_Hora
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
    TomarDatos = Agendar_Hora.objects.all()
    Datos = { "DatosTablaAgendar_Hora":TomarDatos }
    return render(request, "Servicios/Agendar_Hora.html", Datos)

def Agendar_Hora_view(request):
    if request.method == 'POST':
        form =Agendar_HoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Agendar_Hora")
    else:
        form =Agendar_HoraForm()
    return render(request, "Servicios/Agendar_Hora.html", {'form': form})




def Agendar_Hora(request):

        data = {
        'form' :Agendar_HoraForm(),
        }

        if request.method == 'POST':
            formulario = Agendar_HoraForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "guardado correctamente"
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"

            return render(request, "Servicios/Agendar_Hora.html", data)
