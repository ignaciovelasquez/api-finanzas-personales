from django.contrib import admin
from .models import Producto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_creacion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio_estimado', 'disponible', 'categoria', 'fecha_publicacion')
    list_filter = ('disponible', 'categoria')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('fecha_publicacion',)