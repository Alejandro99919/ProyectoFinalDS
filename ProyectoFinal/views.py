# Documento  : ProyectoFinal.
# Autor      : Alejandro Escobar.
# Autor      : Kevin Escobar.
# Fecha      : 26/03/2024
# Ult Mod    : 05/04/2024
# Version    : Beta 0.5
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.http import request
from django.shortcuts import render

def plantillahija1(request):
	return render(request, "plantillaHija1.html", {})


def Login(request):
	return render(request, "Login.html", {})


def crearCuenta(request):
	return render(request, "crearCuenta.html", {})