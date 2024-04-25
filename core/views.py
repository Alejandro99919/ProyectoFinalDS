# Documento  : ProyectoFinal.
# Autor      : Alejandro Escobar.
# Autor      : Kevin Escobar.
# Fecha      : 26/03/2024
# Ult Mod    : 24/04/2024
# Version    : Beta 1.8

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Carros


# Create your views here.
def home(request):
	return render(request, 'core/home.html')

@login_required
def areaempresa(request):
    carro = Carros.objects.all()
    return render(request, 'core/areaempresa.html', {"Vehiculos": carro})

def exit(request):
	logout(request)
	return redirect('home')

def register(request):
	data = {
		'form': CustomUserCreationForm()
	}

	if request.method == 'POST':
		user_creation_form = CustomUserCreationForm(data=request.POST)
		# VALIDA LA INFORMACION
		if user_creation_form.is_valid():
			user_creation_form.save()

			user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
			login(request, user)

			return redirect('home')

	return render(request, 'registration/register.html', data)

def acerca(request):
	return render(request, 'core/Acercade.html')

def registrarCarros(request):
	matricula = request.POST['txtMatricula']
	destino = request.POST['txtDestino']
	cant_paquetes = request.POST['numCant_paquetes']
	carros = Carros.objects.create(matricula=matricula, destino=destino, cant_paquetes=cant_paquetes)
	return redirect('areaempresa')

def eliminarCarro(request, matricula):
	carros = Carros.objects.get(matricula=matricula)
	carros.delete()
	return redirect('areaempresa')