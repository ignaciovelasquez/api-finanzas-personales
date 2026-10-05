from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    # Campo calculado para saber cuántos productos tiene la categoría sin alterar la tabla
    total_productos = serializers.IntegerField(source='productos.count', read_only=True)

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'total_productos']


class ProductoSerializer(serializers.ModelSerializer):
    # Permite mostrar el nombre de la categoría en el JSON además de su ID numérico
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')

    class Meta:
        model = Producto
        fields = [
            'id', 
            'nombre', 
            'descripcion', 
            'precio_estimado', 
            'disponible', 
            'categoria', 
            'categoria_nombre', 
            'fecha_publicacion'
        ]

    # Validación personalizada: previene valores negativos en el precio
    def validate_precio_estimado(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio estimado no puede ser un valor negativo.")
        return value