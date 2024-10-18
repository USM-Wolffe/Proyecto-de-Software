from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Vista para la página de inicio
def index(request):
    return render(request, 'MainApp/index.html')

# Vista para el trabajador
def trabajador(request):
    return render(request, 'MainApp/trabajador.html')

# Vista para el contador
def contador(request):
    return render(request, 'MainApp/contador.html')

# Vista para el jefe de área
def jefe(request):
    return render(request, 'MainApp/jefe.html')

# Vista para la rendicion
def rendicion(request):
    return render(request, 'MainApp/rendicion.html')

# Vista para la rendicion
def ingresar(request):
    return render(request, 'MainApp/ingresar.html')