# API de Finanzas Personales

Backend desarrollado en Django para la gestión y control de finanzas personales.

## Instalación y Ejecución

### 1. Crear y activar el ambiente virtual
```bash
python -m venv .venv

PowerShell
.\.venv\Scripts\activate

2. Instalar dependencias
Bash
pip install django

3. Aplicar migraciones
Bash
python manage.py migrate

4. Ejecutar el servidor
Bash
python manage.py runserver

python manage.py runserver --insecure  #para los archivos estáticos que no salen los estilos debido al debug=false

Rutas de Prueba
Bienvenida: http://127.0.0.1:8000/ (Página principal del proyecto)

Error 404: http://127.0.0.1:8000/ruta-no-existe/ (Pantalla de error controlada)