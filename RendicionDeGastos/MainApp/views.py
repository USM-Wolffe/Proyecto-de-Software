from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gasto, Rendicion
from django.core.paginator import Paginator

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

# Vista para registrar un gasto desde 'rendicion.html'
def rendicion(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo-gasto')
        monto = request.POST.get('monto')
        descripcion = request.POST.get('descripcion')
        documento = request.FILES.get('documento')

        # Guardar el gasto en la base de datos
        Gasto.objects.create(
            tipo=tipo,
            monto=monto,
            descripcion=descripcion,
            documento_respaldo=documento
        )

        # Redirigir a la misma página o a la página de resumen
        return redirect('resumen_rendicion')

    return render(request, 'MainApp/rendicion.html')

# Vista para mostrar el resumen de la rendición
def resumen_rendicion(request):
    # Obtener todos los gastos no asociados a una rendición
    gastos = Gasto.objects.filter(rendicion__isnull=True)
    total = sum(gasto.monto for gasto in gastos)

    # Renderizar la página con los datos
    return render(request, 'MainApp/resumen_rendicion.html', {
        'rendicion': {'id': 'Temporal'},  # ID temporal para el contexto
        'gastos': gastos,
        'total': total
    })

# Vista para registrar la rendición final
def registrar_rendicion(request):
    if request.method == 'POST':
        # Crear una nueva rendición
        rendicion = Rendicion.objects.create(
            estado='Pendiente',  # Estado inicial
            total=0.0  # Este valor se actualizará después
        )

        # Asociar los gastos temporales a esta rendición
        gastos = Gasto.objects.filter(rendicion__isnull=True)
        for gasto in gastos:
            gasto.rendicion = rendicion
            gasto.save()

        # Calcular el total y guardar en la rendición
        rendicion.total = sum(gasto.monto for gasto in gastos)
        rendicion.save()

        # Redirigir a la página de confirmación
        return redirect('exito')

    return HttpResponse('Método no permitido', status=405)

# Vista para ingresar al sistema
def ingresar(request):
    return render(request, 'MainApp/ingresar.html')

# Vista para recuperar la contraseña
def forgot_password(request):
    return render(request, 'MainApp/forgot_password.html')  

# Vista de confirmación de acción exitosa
def exito(request):
    return render(request, 'MainApp/exito.html')  

# Vista para mostrar rendiciones ingresadas con paginación
def rendiciones_ingresadas(request):
    rendiciones = Rendicion.objects.all().order_by('id')  # Orden ascendente
    paginator = Paginator(rendiciones, 6)  # 6 rendiciones por página

    page_number = request.GET.get('page')  # Obtén el número de página de la URL
    page_obj = paginator.get_page(page_number)  # Obtén la página actual

    return render(request, 'MainApp/rendiciones_ingresadas.html', {'page_obj': page_obj})

# Vista para mostrar solo las rendiciones aprobadas
def aprobadas(request):
    rendiciones_aprobadas = Rendicion.objects.filter(estado='Aprobado').order_by('id')  # Solo aprobadas en orden ascendente
    return render(request, 'MainApp/aprobadas.html', {'rendiciones': rendiciones_aprobadas})

# Vista para gestionar reembolsos
def gestion_reembolsos(request):
    if request.method == 'POST':
        rendicion_id = request.POST.get('rendicion_id')
        accion = request.POST.get('accion')

        # Buscar la rendición y actualizar su estado
        rendicion = Rendicion.objects.get(id=rendicion_id)
        if accion == 'aprobar':
            rendicion.estado = 'Aprobado'
        elif accion == 'rechazar':
            rendicion.estado = 'Rechazado'
        rendicion.save()

        # Redirigir a la misma página para reflejar los cambios
        return redirect('gestion_reembolsos')

    # Obtener todas las rendiciones pendientes
    rendiciones_pendientes = Rendicion.objects.filter(estado='Pendiente')

    # Asegurarse de que todas las rendiciones tengan su total correctamente calculado
    for rendicion in rendiciones_pendientes:
        gastos = Gasto.objects.filter(rendicion=rendicion)
        rendicion.total = sum(gasto.monto for gasto in gastos)
        rendicion.save()

    return render(request, 'MainApp/gestion_reembolsos.html', {
        'reembolsos': rendiciones_pendientes
    })

def crear_gasto(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo-gasto')
        monto = request.POST.get('monto')
        descripcion = request.POST.get('descripcion')
        documento = request.FILES.get('documento')

        # Guardar el gasto en la base de datos
        Gasto.objects.create(
            tipo=tipo,
            monto=monto,
            descripcion=descripcion,
            documento_respaldo=documento
        )

        # Redirigir a la página de resumen
        return redirect('resumen_rendicion')

    return HttpResponse('Método no permitido', status=405)
