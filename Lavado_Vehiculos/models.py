from django.db import models

# Create your models here.

class Servicios(models.Model):
    Cliente =models.CharField(max_length=40)
    Productos =models.CharField(max_length=40)
    ValorProducto =models.CharField(max_length=10)
    FechaCompra =models.CharField(max_length=18)
    
class Agendar_Hora(models.Model):
    Cliente =models.CharField(max_length=40)
    Productos =models.CharField(max_length=40)
    ValorProducto =models.CharField(max_length=10)
    FechaCompra =models.CharField(max_length=18)
    

