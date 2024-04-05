# Documento  : ProyectoFinal.
# Autor      : Alejandro Escobar.
# Autor      : Kevin Escobar.
# Fecha      : 26/03/2024
# Ult Mod    : 26/03/2024
# Version    : Beta 0.1
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.http import request
from django.shortcuts import render

def si(request)