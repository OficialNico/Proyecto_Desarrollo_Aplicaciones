from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.forms import ModelForm

# Create your models here.

class Servicios(models.Model):
    Cliente =models.CharField(max_length=40)
    Productos =models.CharField(max_length=40)
    ValorProducto =models.CharField(max_length=10)
    FechaCompra =models.CharField(max_length=18)
    
class Agendar_Hora(models.Model):
    nombre =models.CharField(max_length=40, null=True)
    apellido =models.CharField(max_length=40, null=True)
    telefono =models.CharField(max_length=10, null=True)
    placas =models.CharField(max_length=18, null=True)
    fecha =models.CharField(max_length=18, null=True)
    hora =models.CharField(max_length=18, null=True)
 
class CustomUser(AbstractUser):
    Perfiles =(
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
        ('bodeguero', 'Bodeguero'),
    )

    perfil = models.CharField(max_length=15, choices=Perfiles,default='cliente')
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',  # Agregar related_name único
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',  # Agregar related_name único
        related_query_name='customuser'
    )
    
class Factura(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class ListaFacturas(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    facturas = models.ManyToManyField(Factura)    
