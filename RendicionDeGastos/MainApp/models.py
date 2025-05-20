from django.db import models

# Modelo para representar una Rendición
class Rendicion(models.Model):
    fecha_creacion = models.DateField(auto_now_add=True)  # Fecha en la que se crea la rendición
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Monto total de la rendición
    estado = models.CharField(max_length=20, default='En progreso')  # Estado de la rendición (Ej: En progreso, Confirmada)

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
