from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Primer Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Segundo Nombre',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo Electrónico',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    is_superuser = forms.BooleanField(label='Administrador', required=False)
    is_staff = forms.BooleanField(label='Despachador', required=False, help_text="Conductor = Ninguna de las anteriores")
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'password1', 'password2']

class FormularioEdicionUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser')
        # Excluimos el campo password de forma predeterminada por seguridad
        exclude = ('password',)
    is_staff = forms.BooleanField(label='Despachador', required=False)
    is_superuser = forms.BooleanField(label='Administrador', required=False, help_text="Conductor = Ninguna de las anteriores")
    # is_active = forms.BooleanField(label='Estado Usuario', required=False)