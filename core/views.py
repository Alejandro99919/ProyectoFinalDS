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
from .models import Carros,Envios


# Create your views here.
def home(request):
	return render(request, 'core/home.html')

@login_required
def areaempresa(request):
    carro = Carros.objects.all()
    return render(request, 'core/areaempresa.html', {"Vehiculos": carro})

@login_required
def listadoGeneral(request):
    # Filtrar los vehículos con activo igual a 1
    vehiculos_activos = Carros.objects.all()
    return render(request, 'core/ListadoGeneral.html', {"Vehiculos": vehiculos_activos})


@login_required
def listadoEliminados(request):
    # Filtrar los vehículos con activo igual a 1
    vehiculos_activos = Carros.objects.filter(estado='Eliminado')
    return render(request, 'core/ListadoEliminados.html', {"Vehiculos": vehiculos_activos})

@login_required
def listadoMantenimiento(request):
    # Filtrar los vehículos con activo igual a 1
    vehiculos_activos = Carros.objects.filter(estado='Mantenimiento')
    return render(request, 'core/ListadoMantenimiento.html', {"Vehiculos": vehiculos_activos})

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
	modelo = request.POST['txtModelo']
	anioFabricacion = request.POST['txtAnioFabricacion']
	carros = Carros.objects.create(matricula=matricula, modelo=modelo, anioFabricacion=anioFabricacion)
	return redirect('areaempresa')

def registrarEnvio(request):
    paquetes_pequeños = request.POST['txtPaquetesPequeños']
    paquetes_grandes = request.POST['txtPaquetesGrandes']
    paquetes_fragiles = request.POST['txtPaquetesFragiles']
    destino = request.POST['txtDestino']
    vehiculo_asignado = request.POST['txtVehiculoAsignado']
    envios = Envios.objects.create(
        paquetes_pequeños=paquetes_pequeños,
        paquetes_grandes=paquetes_grandes,
        paquetes_fragiles=paquetes_fragiles,
        destino=destino,
        vehiculo_asignado=vehiculo_asignado
    )
    vehiculo = Carros.objects.get(matricula=vehiculo_asignado)
    if vehiculo.matricula == vehiculo_asignado and destino == 'Buga-Pereira' and vehiculo.cargaActual > 40:
        vehiculo.cargaActual= (vehiculo.cargaActual - 40)
        vehiculo.save()
        return redirect('areaempresa')
    elif vehiculo.matricula == vehiculo_asignado and destino == 'Buga-Cali' and vehiculo.cargaActual > 70:
        vehiculo.cargaActual= (vehiculo.cargaActual - 70)
        vehiculo.save()
        return redirect('areaempresa')
    else:
        # Mostrar alerta de carga insuficiente (implementa esto en tu HTML/JS)
        return redirect('areaempresa')




	
def eliminarCarro(request, matricula):
	carros = Carros.objects.get(matricula=matricula)
	carros.estado="Eliminado"
	carros.save();
	return redirect('areaempresa')

def edicionCarro(request, matricula):
    carros = Carros.objects.get(matricula=matricula)
    return render(request, "core/EdicionVehiculo.html", {"carros": carros})

def editarCarros(request):
	matricula = request.POST['txtMatricula']
	modelo = request.POST['txtModelo']
	estado= request.POST['txtEstado']
	anioFabricacion = request.POST['txtAnio_Fabricacion']
	carga_actual= request.POST['txtCarga_Actual']
	carros = Carros.objects.get(matricula=matricula)
	carros.modelo = modelo
	carros.estado = estado
	carros.anioFabricacion = anioFabricacion
	carros.cargaActual = carga_actual
	carros.save()
	return redirect('areaempresa')


def cargarCarros(request,matricula):
	carros = Carros.objects.get(matricula=matricula)
	carros.cargaActual=100
	carros.save()
	return redirect('areaempresa')