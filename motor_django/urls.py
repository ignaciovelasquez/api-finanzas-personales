from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'),
    path('api/', include('api.urls')),  # Conecta todos los endpoints de DRF
]