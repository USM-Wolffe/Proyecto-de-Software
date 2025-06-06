from django.urls import path
from .views import (
    index,
    trabajador,
    contador,
    jefe,
    rendicion,
    ingresar,
    forgot_password,
    exito,
    rendiciones_ingresadas,
    gestion_reembolsos,
    resumen_rendicion,
    registrar_rendicion,
    crear_gasto,
    aprobadas,
    ingresador,
    visualizador,
    estadisticas,
    generar_informe
)

urlpatterns = [
    path('', index, name='index'),  # Ruta para la página de inicio
    path('trabajador/', trabajador, name='trabajador'),  # Ruta para la vista del trabajador
    path('contador/', contador, name='contador'),  # Ruta para la vista del contador
    path('jefe/', jefe, name='jefe'),  # Ruta para la vista del jefe
    path('rendicion/', rendicion, name='rendicion'),
    path('ingresar/', ingresar, name='ingresar'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('exito/', exito, name='exito'),
    path('rendiciones/', rendiciones_ingresadas, name='rendiciones_ingresadas'),
    path('gestion-reembolsos/', gestion_reembolsos, name='gestion_reembolsos'),
    path('resumen_rendicion/', resumen_rendicion, name='resumen_rendicion'),
    path('registrar-rendicion/', registrar_rendicion, name='registrar_rendicion'),
    path('crear-gasto/', crear_gasto, name='crear_gasto'),  # NUEVO
    path('aprobadas/', aprobadas, name='aprobadas'),  # FIX: usar la vista importada directamente
    path('ingresador/', ingresador, name='ingresador'),
    path('visualizador/', visualizador, name='visualizador'),
    path('estadisticas/', estadisticas, name='estadisticas'),
    path('generar-informe/', generar_informe, name='generar_informe'),
]
