# Documento  : ProyectoFinal.
# Autor      : Alejandro Escobar.
# Autor      : Kevin Escobar.
# Fecha      : 26/03/2024
# Ult Mod    : 18/04/2024
# Version    : Beta 1.3

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home(request):
	return render(request, 'core/home.html')

@login_required
def areaempresa(request):
	return render(request, 'core/areaempresa.html')

def exit(request):
	logout(request)
	return redirect('home')