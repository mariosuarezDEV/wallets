from django.db import models
from django.contrib.auth.models import User
from base.models import Auditoria
# Create your models here.

class Billeteras(Auditoria):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, help_text="Usuario propietario de la billetera", related_name="billetera", verbose_name="Usuario", null=False, blank=False)
    nombre = models.CharField(max_length=50, help_text="Nombre de la billetera", verbose_name="Nombre", null=False, blank=False)
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la billetera", verbose_name="Descripción")

    def __str__(self):
        return f'Billetera de {self.usuario.username}'
    class Meta:
        verbose_name = "Billetera"
        verbose_name_plural = "Billeteras"

class FormasPago(Auditoria):
    nombre = models.CharField(max_length=50, help_text="Nombre de la forma de pago", verbose_name="Nombre", null=False, blank=False)
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la forma de pago", verbose_name="Descripción")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Saldo disponible en la forma de pago", verbose_name="Saldo")
    billetera = models.ForeignKey(Billeteras, on_delete=models.PROTECT, help_text="Billetera asociada a la forma de pago", related_name="formas_pago", verbose_name="Billetera", null=False, blank=False)
    def __str__(self):
        return f'{self.nombre} - {self.billetera.usuario.username}'
    class Meta:
        verbose_name = "Forma de Pago"
        verbose_name_plural = "Formas de Pago"
        ordering = ['nombre']

TIPO_TRANSACCION = (
    ('I', 'Ingreso'),
    ('G', 'Gasto'),
)

# Mangers para las transacciones
class IngresosManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='I')

class GastosManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='G')

class Transacciones(Auditoria):
    forma_pago = models.ForeignKey(FormasPago, on_delete=models.PROTECT, help_text="Forma de pago utilizada en la transacción", related_name="transacciones", verbose_name="Forma de Pago", null=False, blank=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monto de la transacción", verbose_name="Monto", null=False, blank=False)
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la transacción", verbose_name="Descripción")
    fecha_movimiento = models.DateField(help_text="Fecha y hora de la transacción", verbose_name="Fecha", null=False, blank=False, auto_now_add=True)
    tipo = models.CharField(max_length=3, choices=TIPO_TRANSACCION, help_text="Tipo de transacción", verbose_name="Tipo", null=False, blank=False)
    # Manejador personalizado para las transacciones
    objects = models.Manager()  # Manejador por defecto
    ingresos = IngresosManager() # Manejador para ingresos
    gastos = GastosManager() # Manejador para gastos
    def __str__(self):
        return f'Transacción en {self.forma_pago.nombre} con un total de ${self.monto} ({self.tipo})'
    class Meta:
        verbose_name = "Transacción"
        verbose_name_plural = "Transacciones"