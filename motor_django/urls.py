from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Vista Pública Principal
    path('', views.bienvenida, name='bienvenida'),
    
    # 2. Rutas del Sistema de Autenticación (Login / Logout)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # 3. Vistas Privadas Protegidas
    path('dashboard/', views.dashboard_privado, name='dashboard'),  # FBV con @login_required
    path('gestion-productos/', views.GestionProductosPrivadaView.as_view(), name='gestion_productos'),  # CBV con LoginRequiredMixin
    
    # 4. Endpoints de la API REST (DRF)
    path('api/', include('api.urls')),
]