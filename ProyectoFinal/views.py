# Documento  : ProyectoFinal.
# Autor      : Alejandro Escobar.
# Autor      : Kevin Escobar.
# Fecha      : 26/03/2024
# Ult Mod    : 01/05/2024
# Version    : Beta 2.1

from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def plantillahija1(request):
	return render(request, "plantillaHija1.html", {})