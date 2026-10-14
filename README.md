# API REST de Finanzas Personales & Sistema de Control de Acceso

Servicio Backend desarrollado con **Python**, **Django** y **Django REST Framework (DRF)** con persistencia en **MySQL**, desacoplamiento de credenciales sensibles mediante **python-decouple** y sistema completo de **Autenticación y Control de Acceso (FBV / CBV)**.

---

## 1. Requerimientos Técnicos

- Python 3.10+
- Django 6.1+
- Django REST Framework 3.18+
- MySQL / MariaDB (XAMPP / Standalone en puerto 3306)
- mysqlclient 2.3+
- python-decouple 3.8+

---

## 2. Configuración de Base de Datos (Scripts SQL)

El proyecto incluye scripts independientes en la carpeta `scripts/`:

1. `scripts/01_create_db.sql`: Creación de la base de datos `finanzas_db`.
2. `scripts/02_create_user.sql`: Creación del usuario `finanzas_user`.
3. `scripts/03_grant_privileges.sql`: Otorgamiento de privilegios para `finanzas_user`.
4. `scripts/01_init_db.sql`: Script unificado para inicialización en un solo paso.

```sql
CREATE DATABASE IF NOT EXISTS finanzas_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'finanzas_user'@'localhost' IDENTIFIED BY 'Futbol123';
GRANT ALL PRIVILEGES ON finanzas_db.* TO 'finanzas_user'@'localhost';
FLUSH PRIVILEGES;
```

---

## 3. Variables de Entorno (`.env`)

El archivo `.env` se gestiona mediante `python-decouple`. Copiar la plantilla base `.env.example`:

```env
SECRET_KEY=django-insecure-tu-clave-aqui-123456
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=django.db.backends.mysql
DB_NAME=finanzas_db
DB_USER=finanzas_user
DB_PASSWORD=Futbol123
DB_HOST=localhost
DB_PORT=3306
```

---

## 4. Instalación y Puesta en Marcha

### 4.1 Entorno Virtual y Dependencias
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 4.2 Migraciones y Creación de Superusuario
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4.3 Ejecución del Servidor
```powershell
python manage.py runserver
```

---

## 5. Rutas y Control de Acceso del Sistema

### 5.1 Vistas Web Públicas y Privadas
| Ruta | Tipo | Protección | Descripción |
| :--- | :---: | :---: | :--- |
| `/` | FBV | **Pública** | Landing page de bienvenida y resumen del sistema. |
| `/login/` | Auth | **Pública** | Formulario de autenticación con `LoginView`. |
| `/logout/` | Auth | **Pública** | Cierre de sesión con `LogoutView` y redirección. |
| `/dashboard/` | FBV | **Privada (`@login_required`)** | Métricas financieras y resumen para usuarios autenticados. |
| `/gestion-productos/` | CBV | **Privada (`LoginRequiredMixin`)** | Catálogo y administración de productos (ListView). |
| `/admin/` | Admin | **Staff/Superuser** | Panel de administración oficial de Django. |

### 5.2 Endpoints de la API REST (DRF)
| Recurso | Método HTTP | Endpoint | Descripción |
| :--- | :---: | :--- | :--- |
| **Raíz API** | `GET` | `/api/` | Browsable API de Django REST Framework |
| **Categorías** | `GET` / `POST` | `/api/categorias/` | Listar y crear categorías |
| **Categoría** | `GET` / `PUT` / `PATCH` / `DELETE` | `/api/categorias/{id}/` | Detalle, edición y borrado de categoría |
| **Productos** | `GET` / `POST` | `/api/productos/` | Listar y registrar productos |
| **Producto** | `GET` / `PUT` / `PATCH` / `DELETE` | `/api/productos/{id}/` | Detalle, edición y borrado de producto |