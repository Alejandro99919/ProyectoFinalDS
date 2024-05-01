"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from ProyectoFinal.views import plantillahija1
from . import views
from .views import home, areaempresa, exit, register, acerca, registrarCarros, registrarEnvio, eliminarCarro, eliminarEnvio, edicionCarro, edicionEnvio, editarCarros, editarEnvios, cargarCarros, listadoGeneral, listadoEliminados, listadoMantenimiento, listadoEnvios, listadoEnviosEliminados, mostrarVehiculo, consultaPKEnvios, consultaPKVehiculos, DatosUser, listadoUsuariosGeneral, listadoUsuariosEliminados, listadoUsuariosConductor, listadoUsuariosDespachadores, listadoUsuariosAdministradores, listadoUsuarioId, EliminacionUsuario, EdicionUsuario, ActivacionUsuario

urlpatterns = [
    path('', home, name='home'),
    path('areaempresa/', areaempresa, name='areaempresa'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('acerca/', acerca, name='acerca'),
    path('registrarCarros/', registrarCarros, name='registrarCarros'),
    path('areaempresa/eliminarCarro/<str:matricula>/', eliminarCarro, name='eliminarCarro'),
    path('areaempresa/edicionCarro/<str:matricula>/', edicionCarro, name='edicionCarro'),
    path('areaempresa/edicionEnvio/<str:id_envio>/', edicionEnvio, name='edicionEnvio'),
    path('areaempresa/eliminarEnvio/<str:id_envio>/', eliminarEnvio, name='eliminarEnvio'),
    path('editarCarros/', editarCarros, name='editarCarros'),
    path('editarEnvios/', editarEnvios, name='editarEnvios'),
    path('listadoGeneral/',listadoGeneral, name='listadoGeneral'),
    path('listadoEliminados/',listadoEliminados, name='listadoEliminados'),
    path('listadoMantenimiento/',listadoMantenimiento, name='listadoMantenimiento'),
    path('listadoEnvios/',listadoEnvios,name='listadoEnvios'),
    path('listadoEnviosEliminados/',listadoEnviosEliminados, name='listadoEnviosEliminados'),
    path('consultaPKEnvios/',consultaPKEnvios,name="consultaPKEnvios"),
    path('areaempresa/cargarCarros/<str:matricula>/', cargarCarros, name='cargarCarros'),
    path('registrarEnvio/', registrarEnvio, name='registrarEnvio'),
    path('consultaPKEnvios/', consultaPKEnvios, name='consultaPKEnvios'),
    path('consultaPKVehiculos/', consultaPKVehiculos, name='consultaPKVehiculos'),
    path('DatosUser/', DatosUser, name='DatosUser'),
    path('listadoUsuariosGeneral/', listadoUsuariosGeneral, name='listadoUsuariosGeneral'),
    path('listadoUsuariosEliminados/', listadoUsuariosEliminados, name='listadoUsuariosEliminados'),
    path('listadoUsuariosConductor/', listadoUsuariosConductor, name='listadoUsuariosConductor'),
    path('listadoUsuariosDespachadores/', listadoUsuariosDespachadores, name='listadoUsuariosDespachadores'),
    path('listadoUsuariosAdministradores/', listadoUsuariosAdministradores, name='listadoUsuariosAdministradores'),
    path('listadoUsuarioId/', listadoUsuarioId, name='listadoUsuarioId'),
    path('listadoUsuariosGeneral/EliminacionUsuario/<int:id_usuario>', EliminacionUsuario, name='EliminacionUsuario'),
    path('listadoUsuariosGeneral/EdicionUsuario/<int:id_usuario>', EdicionUsuario, name='EdicionUsuario'),
    path('listadoUsuariosGeneral/ActivacionUsuario/<int:id_usuario>', ActivacionUsuario, name='ActivacionUsuario'),
]



