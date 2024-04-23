from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Primer Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Segundo Nombre',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo Electrónico',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
