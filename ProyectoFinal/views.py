# Documento  : ProyectoFinal.
# Autor      : Alejandro Escobar.
# Autor      : Kevin Escobar.
# Fecha      : 26/03/2024
# Ult Mod    : 09/04/2024
# Version    : Beta 1.0
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.http import request
from django.shortcuts import render

def plantillahija1(request):
	return render(request, "plantillaHija1.html", {})

def Login(request):
	return render(request, "Login.html", {})