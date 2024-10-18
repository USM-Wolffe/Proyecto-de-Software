from django.urls import path
from .views import index, trabajador, contador, jefe, rendicion,ingresar

urlpatterns = [
    path('', index, name='index'),  # Ruta para la página de inicio
    path('trabajador/', trabajador, name='trabajador'),  # Ruta para la vista del trabajador
    path('contador/', contador, name='contador'),  # Ruta para la vista del contador
    path('jefe/', jefe, name='jefe'),  # Ruta para la vista del jefe
    path('rendicion/', rendicion, name='rendicion'),  
    path('ingresar/', ingresar, name='ingresar'),  
]
