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

def forgot_password(request):
    return render(request, 'MainApp/forgot_password.html')  

def exito(request):
    return render(request, 'MainApp/exito.html')  

def rendiciones_ingresadas(request):
    rendiciones = [
        {'id': 1, 'nombre': 'Rendición 1', 'estado': 'Aprobado'},
        {'id': 2, 'nombre': 'Rendición 2', 'estado': 'Rechazado'},
        {'id': 3, 'nombre': 'Rendición 3', 'estado': 'Aprobado'},
        {'id': 4, 'nombre': 'Rendición 4', 'estado': 'Pendiente'},
    ]
    return render(request, 'MainApp/rendiciones_ingresadas.html', {'rendiciones': rendiciones})

def gestion_reembolsos(request):
    # Datos ficticios para mostrar en la tabla
    reembolsos = [
        {
            'numero': '05/10/2023',
            'nombre': 'Wide World Importers',
            'fecha': 'Redes',
            'monto': '111,001',
            'estado': '250,001'
        }
    ]
    return render(request, 'MainApp/gestion_reembolsos.html', {'reembolsos': reembolsos})

def resumen_rendicion(request):
    return render(request, 'MainApp/resumen_rendicion.html')  