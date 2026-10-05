from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

# --- Vista Web HTML de Bienvenida (Evaluación 1) ---
def bienvenida(request):
    return render(request, 'bienvenida.html')

# --- ViewSets de la API REST (Evaluación 2) ---
class CategoriaViewSet(viewsets.ModelViewSet):
    """
    Controlador CRUD para el recurso Categorías.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """
    Controlador CRUD para el recurso Productos.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer