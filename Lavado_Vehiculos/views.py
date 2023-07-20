from django.shortcuts import render
from.models import Servicios, Agendar_Hora

# Create your views here.


def Servicios(request):
    TomarDatos = Servicios.objects.all()
    Datos = { "DatosTabla":TomarDatos }
    return render(request, "TemplatesHtml/Servicios.html", Datos)

def Agendar_Hora(request):
    TomarDatos = Agendar_Hora.objects.all()
    Datos = { "DatosTabla":TomarDatos }
    return render(request, "TemplatesHtml/Agendar_Hora.html", Datos)



