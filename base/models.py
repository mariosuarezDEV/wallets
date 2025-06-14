from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Auditoria(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación del registro", verbose_name="Fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, help_text="Fecha de modificación del registro", verbose_name="Fecha de modificación")
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, help_text="Usuario que creó el registro", related_name="%(class)s_creacion", verbose_name="Usuario de creación", null=True, blank=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.PROTECT, help_text="Usuario que modificó el registro", related_name="%(class)s_modificacion", verbose_name="Usuario de modificación", null=True, blank=True)
    notas = models.TextField(blank=True, null=True, help_text="Notas adicionales sobre el registro", verbose_name="Notas")
    visible = models.BooleanField(default=True, help_text="Indica si el registro es visible", verbose_name="Visible")
    class Meta:
        abstract = True
        ordering = ['-fecha_creacion']
        verbose_name = "Auditoría"
        verbose_name_plural = "Auditorías"