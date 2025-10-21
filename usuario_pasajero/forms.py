from django import forms
from .models import UsuarioPasajero  

class UsuarioPasajeroForm(forms.ModelForm):
    class Meta:
        model = UsuarioPasajero 
        fields = ['nombre', 'email', 'telefono', 'fecha_registro']
        labels = {
            'nombre': 'Nombre',
            'email': 'Email',
            'telefono': 'Telefono',
            'fecha_registro': 'Fecha de Registro',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_registro': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }