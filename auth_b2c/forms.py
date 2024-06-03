from django import forms
from django.contrib.auth.forms import UserCreationForm
from auth_b2c.models import Perfil

class RegistroForm(UserCreationForm):
    username = forms.CharField(label='Nombre', required=True, widget=forms.TextInput)
    password1 = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', required=True, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email' ,required=True, widget=forms.EmailInput)
    first_name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput)
    last_name = forms.CharField(label='Apellido', required=True, widget=forms.TextInput)
    nacimiento = forms.DateField(label='Fecha de nacimiento', required=True, widget=forms.DateInput(attrs={'type':'date'}))
    
    class Meta:
        
        model = Perfil
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'nacimiento']
        #help_texts = {k:"" for k in fields}