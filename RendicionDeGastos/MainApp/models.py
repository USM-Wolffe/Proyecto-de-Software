from django.db import models

# Modelo para representar una Rendición
class Rendicion(models.Model):
    """Representa una rendición de gastos."""

    ESTADO_INGRESADA = 'Ingresada'
    ESTADO_PENDIENTE = 'Pendiente'
    ESTADO_APROBADO = 'Aprobado'
    ESTADO_RECHAZADO = 'Rechazado'

    ESTADOS_CHOICES = [
        (ESTADO_INGRESADA, 'Ingresada'),
        (ESTADO_PENDIENTE, 'Pendiente'),
        (ESTADO_APROBADO, 'Aprobado'),
        (ESTADO_RECHAZADO, 'Rechazado'),
    ]

    fecha_creacion = models.DateField(auto_now_add=True)  # Fecha en la que se crea la rendición
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Monto total de la rendición
    # Estado de la rendición (controla las fases Ingreso/Validación)
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default=ESTADO_INGRESADA)

    def __str__(self):
        return f"Rendición {self.id} - {self.estado}"


# Modelo para representar un Gasto
class Gasto(models.Model):
    tipo = models.CharField(max_length=50)  # Tipo de gasto (Ej: Transporte, Alimentación)
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Monto del gasto
    descripcion = models.TextField(max_length=200, blank=True)  # Descripción opcional del gasto
    documento_respaldo = models.FileField(upload_to='documentos/', blank=True, null=True)  # Archivo opcional como respaldo del gasto
    rendicion = models.ForeignKey(
        Rendicion,
        on_delete=models.CASCADE,
        related_name='gastos',
        null=True,
        blank=True
    )  # Relación opcional con una rendición (gasto temporal si está en blanco)

    def __str__(self):
        return f"{self.tipo} - ${self.monto}"
