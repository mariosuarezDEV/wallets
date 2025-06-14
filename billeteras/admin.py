from django.contrib import admin
from .models import Billeteras, FormasPago, Transacciones
# Register your models here.

@admin.register(Billeteras)
class BilleterasAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'descripcion', 'fecha_creacion', 'fecha_modificacion', 'visible')
    search_fields = ('usuario__username', 'nombre')
    list_filter = ('fecha_creacion', 'fecha_modificacion', 'visible')
    ordering = ('-fecha_creacion',)
@admin.register(FormasPago)
class FormasPagoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'balance', 'billetera', 'fecha_creacion', 'fecha_modificacion', 'visible')
    search_fields = ('nombre', 'billetera__usuario__username')
    list_filter = ('fecha_creacion', 'fecha_modificacion', 'visible')
    ordering = ('-fecha_creacion',)
@admin.register(Transacciones)
class TransaccionesAdmin(admin.ModelAdmin):
    list_display = ('forma_pago', 'monto', 'descripcion', 'fecha_movimiento', 'tipo', 'fecha_creacion', 'fecha_modificacion', 'visible')
    search_fields = ('forma_pago__nombre', 'descripcion')
    list_filter = ('fecha_movimiento', 'tipo', 'fecha_creacion', 'fecha_modificacion', 'visible')
    ordering = ('-fecha_movimiento',)