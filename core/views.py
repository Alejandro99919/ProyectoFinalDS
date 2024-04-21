# Documento  : ProyectoFinal.
# Autor      : Alejandro Escobar.
# Autor      : Kevin Escobar.
# Fecha      : 26/03/2024
# Ult Mod    : 20/04/2024
# Version    : Beta 1.5

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from.forms import CustomUserCreationForm

# Create your views here.
def home(request):
	return render(request, 'core/home.html')

@login_required
def areaempresa(request):
	return render(request, 'core/areaempresa.html')

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

			return redirect('home')

	return render(request, 'registration/register.html', data)