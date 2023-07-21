from django import forms
from .models import Agendar_Hora

class Agendar_HoraForm(forms.ModelForm):
    class Meta:
        model = Agendar_Hora
        fields = '__all__'
