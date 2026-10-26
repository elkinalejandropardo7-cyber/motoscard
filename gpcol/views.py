from django.shortcuts import render
from .models import Piloto
# Create your views here.

# views.py

def index(request):
    # Consultamos todos los pilotos registrados
    pilotos = Piloto.objects.all()

    # Pasamos los pilotos al diccionario de contexto
    contexto = {
        'pilotos': pilotos
    }

    return render(request, 'gpcol/index.html', contexto)