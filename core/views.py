# Documento  : ProyectoFinal.
# Autor      : Alejandro Escobar.
# Autor      : Kevin Escobar.
# Fecha      : 26/03/2024
# Ult Mod    : 30/04/2024
# Version    : Beta 2.0

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Carros,Envios
from django.contrib.auth import get_user_model

# Create your views here.

def home(request):
	return render(request, 'core/home.html')

@login_required
def areaempresa(request):
    if request.user.is_superuser or request.user.is_staff:
        carro = Carros.objects.all()
        return render(request, 'core/areaempresa.html', {"Vehiculos": carro})
    else:
        return render(request, 'core/areaempresaConductor.html')

@login_required
def edicionEnvio(request):
    envios = Envios.objects.all()
    return render(request, 'core/edicionEnvio.html', {"Envios": envios})

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

@login_required
def listadoEnvios(request):
    envios = Envios.objects.all()
    return render(request, 'core/ListadoEnvios.html', {"Envios": envios})

@login_required
def listadoEnviosEliminados(request):
    envios = Envios.objects.filter(estado='Eliminado')
    return render(request, 'core/ListadoEnviosEliminados.html', {"Envios": envios})

def exit(request):
	logout(request)
	return redirect('home')

def register(request):
    # Verifica si el usuario está logueado
    if not request.user.is_authenticated:
        return redirect('login')  # Redirigir a la página de login si no está loggeado
     # Verifica si el usuario actual es superusuario
    if request.user.is_superuser:
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
    else:
        # Si no es superusuario, mostrar mensaje de acceso denegado
        return render(request, 'core/acceso_denegado.html')

def acerca(request):
	return render(request, 'core/Acercade.html')

@login_required
def registrarCarros(request):
    if request.method == 'POST':
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

    # Validar el vehículo asignado con la tabla Carros
    carros = Carros.objects.filter(matricula=vehiculo_asignado)
    if not carros:
        return redirect('areaempresa')

    carro = carros[0]

    # Si la carga actual del carro es mayor o igual a 80, restarle el valor correspondiente
   # Si la carga actual del carro es mayor o igual a 80, restarle el valor correspondiente
    # Si la carga actual del carro es mayor o igual a 80, restarle el valor correspondiente
    if carro.cargaActual >= 40:
        if destino == 'Buga-Pereira':
            carro.cargaActual =(carro.cargaActual - 40)
    if carro.cargaActual >=50:
        if destino == 'Buga-Cali':
            carro.cargaActual = (carro.cargaActual - 50)
    if carro.cargaActual >=80:
        if destino =='Buga-Medellín':
            carro.cargaActual = (carro.cargaActual - 80)
    if carro.cargaActual >=80:        
        if destino == 'Cali-Bogotá':
            carro.cargaActual = (carro.cargaActual - 60)
            
    if carro.cargaActual >=70:
        if destino == 'Bogotá-Medellín':
            carro.cargaActual =(carro.cargaActual-70)
            
    if carro.cargaActual >=65:
        if destino == 'Medellín-Bogotá':
            carro.cargaActual = (carro.cargaActual-65)
    if carro.cargaActual >=55:
        if destino == 'Cali-Buga':
            carro.cargaActual = (carro.cargaActual-55)

    carro.save()
    envios = Envios.objects.create(
        paquetes_pequeños=paquetes_pequeños,
        paquetes_grandes=paquetes_grandes,
        paquetes_fragiles=paquetes_fragiles,
        destino=destino,
        vehiculo_asignado=vehiculo_asignado
    )
    envios.save()
    
    return redirect('areaempresa')


def eliminarCarro(request, matricula):
	carros = Carros.objects.get(matricula=matricula)
	carros.estado="Eliminado"
	carros.save();
	return redirect('areaempresa')

def eliminarEnvio(request, id_envio):
	envios = Envios.objects.get(id_envio=id_envio)
	envios.estado="Eliminado"
	envios.save();
	return redirect('areaempresa')




def edicionCarro(request, matricula):
    carros = Carros.objects.get(matricula=matricula)
    return render(request, "core/EdicionVehiculo.html", {"carros": carros})

def edicionEnvio(request, id_envio):
    envio = Envios.objects.get(id_envio=id_envio)
    envios = Envios.objects.all()
    return render(request, 'core/edicionEnvio.html', {'envio': envio, 'envios': envios})

def consultaPKEnvios(request):
    envio = None
    if request.method == 'POST':
        id_envio = request.POST.get('id_envio')
        envio = Envios.objects.filter(pk=id_envio).first()

    return render(request, 'core/ConsultaPKEnvios.html', {'envio': envio})


def consultaPKVehiculos(request):
    carro = None  # Inicializa 'carro' a None
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        carro = Carros.objects.filter(matricula=matricula).first()

    return render(request, 'core/ConsultaPKVehiculos.html', {'carro': carro})

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


def editarEnvios(request):
    id_envio = request.POST['txtID_Envio']
    paquetes_pequeños = request.POST['txtPaquetesPequeños']
    paquetes_grandes = request.POST['txtPaquetesGrandes']
    paquetes_fragiles = request.POST['txtPaquetesFragiles']
    destino = request.POST['txtDestino']
    vehiculo_asignado = request.POST['txtVehiculoAsignado']
    estado = request.POST['txtEstado']
    envios = Envios.objects.get(id_envio=id_envio)
    envios.paquetes_pequeños = paquetes_pequeños
    envios.paquetes_grandes = paquetes_grandes
    envios.paquetes_fragiles = paquetes_fragiles
    envios.destino = destino
    envios.vehiculo_asignado = vehiculo_asignado
    envios.estado = estado
    envios.save()
    return redirect('areaempresa')

def cargarCarros(request,matricula):
	carros = Carros.objects.get(matricula=matricula)
	carros.cargaActual=100
	carros.save()
	return redirect('areaempresa')

def mostrarVehiculo(request,pk):
   vehiculo = get_object_or_404(Carros, pk=pk)
   return render(request, 'ConsultaPKEnvios.html',{'vehiculo':vehiculo})


# def acceso_denegado(request):