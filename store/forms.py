from django import forms
from django.contrib.auth.forms import UserCreationForm
from auth_b2c.models import Perfil

class PerfilForm(forms.ModelForm):
    imagen = forms.ImageField(label='Imagen de perfil', required=False)
    portada = forms.ImageField(label='Foto de portada', required=False)
    nacimiento = forms.DateField(label='Fecha de nacimiento', required=False, widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = Perfil
        fields = ['imagen', 'portada', 'nacimiento']  # Incluye el nuevo campo