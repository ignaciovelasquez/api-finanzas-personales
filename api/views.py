from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from rest_framework import viewsets
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

# --- Vista Web HTML de Bienvenida (Pública) ---
def bienvenida(request):
    """Vista pública principal (Landing Page)."""
    return render(request, 'bienvenida.html')


# --- Vista Basada en Función (FBV) Protegida ---
@login_required
def dashboard_privado(request):
    """
    FBV protegida mediante @login_required:
    Calcula totales de Categorías y Productos, y lista los registros recientes.
    """
    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()
    productos_recientes = Producto.objects.select_related('categoria').order_by('-fecha_publicacion')[:5]

    contexto = {
        'usuario': request.user,
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'productos_recientes': productos_recientes,
    }
    return render(request, 'dashboard.html', contexto)


# --- Vista Basada en Clase (CBV) Protegida ---
class GestionProductosPrivadaView(LoginRequiredMixin, ListView):
    """
    CBV protegida mediante LoginRequiredMixin:
    Lista el catálogo completo de productos con su categoría asociada.
    """
    model = Producto
    template_name = 'gestion_productos.html'
    context_object_name = 'productos'
    paginate_by = 10

    def get_queryset(self):
        return Producto.objects.select_related('categoria').order_by('nombre')


# --- ViewSets de la API REST (DRF) ---
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