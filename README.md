# API REST de Finanzas Personales

Servicio Backend desarrollado con **Python**, **Django** y **Django REST Framework (DRF)** con persistencia en MySQL y desacoplamiento de credenciales sensibles mediante variables de entorno.

---

## 1. Requerimientos Técnicos

- Python 3.10+
- Django 6.x
- Django REST Framework 3.15+
- MySQL / MariaDB (XAMPP en puerto 3306)
- mysqlclient
- python-dotenv

---

## 2. Configuración de Base de Datos (Scripts SQL)

El proyecto incluye en `scripts/01_init_db.sql` las sentencias para crear la base de datos, el usuario y sus permisos:

```sql
CREATE DATABASE IF NOT EXISTS finanzas_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'finanzas_user'@'localhost' IDENTIFIED BY 'Futbol123';
GRANT ALL PRIVILEGES ON finanzas_db.* TO 'finanzas_user'@'localhost';
FLUSH PRIVILEGES;
```
3. Variables de Entorno
Crear el archivo .env en la raíz tomando como base .env.example:

Fragmento de código
SECRET_KEY=django-insecure-tu-clave-aqui-123456
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=django.db.backends.mysql
DB_NAME=finanzas_db
DB_USER=finanzas_user
DB_PASSWORD=Su_contrasena_aqui
DB_HOST=localhost
DB_PORT=3306
4. Instalación y Puesta en Marcha
4.1 Entorno virtual y dependencias
PowerShell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
4.2 Migraciones y arranque
PowerShell
python manage.py makemigrations api
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
5. Endpoints de la API REST
Ruta base navegable (DRF Browsable API): http://127.0.0.1:8000/api/

Categorías:

GET /api/categorias/ - Listar todas las categorías

POST /api/categorias/ - Crear categoría

GET / PUT / PATCH / DELETE /api/categorias/{id}/ - Detalle, edición y borrado

Productos:

GET /api/productos/ - Listar todos los productos

POST /api/productos/ - Registrar nuevo producto

GET / PUT / PATCH / DELETE /api/productos/{id}/ - Detalle, edición y borrado

Administración y Web:

Panel Admin: http://127.0.0.1:8000/admin/

Bienvenida: http://127.0.0.1:8000/