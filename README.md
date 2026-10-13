# Plataforma de Música

## Proyecto de Programación Backend

**Asignatura:** Programación Backend
**Docente:** Erick Bailey Rebolledo
**Evaluaciones:** N.° 2 y N.° 3
**Tecnologías:** Python, Django, Django REST Framework y MySQL

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo del backend de una Plataforma de Música utilizando Django y Django REST Framework.

La aplicación permite administrar información relacionada con usuarios, artistas, géneros musicales, álbumes, canciones, playlists y otras funcionalidades de una plataforma musical.

El sistema utiliza una API REST para realizar operaciones CRUD sobre los modelos de datos y una base de datos MySQL para almacenar la información.

También incorpora autenticación de usuarios, inicio y cierre de sesión, registro y control de acceso a determinadas vistas y endpoints.

## 2. Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- MySQL
- HTML
- Git y GitHub
- Visual Studio Code

## 3. Estructura del proyecto

```text
BackEnd-Django/
│
├── motor_django/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── Plataforma_de_musica/
│   ├── migrations/
│   ├── templates/
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   └── registro.html
│   │   ├── base.html
│   │   ├── bienvenida.html
│   │   ├── dashboard.html
│   │   └── 404.html
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── sql/
│   ├── 01_crear_bd.sql
│   ├── 02_crear_usuario.sql
│   └── 03_permisos.sql
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

El archivo `.env` se mantiene de forma local y no se publica en el repositorio.

## 4. Modelo de datos

La aplicación utiliza los siguientes modelos:

- **Usuario:** almacena información de los usuarios de la plataforma musical.
- **Artista:** registra los artistas musicales.
- **Genero:** permite clasificar la música por género.
- **Album:** almacena información de los álbumes.
- **Cancion:** registra las canciones.
- **Playlist:** permite organizar listas de reproducción.
- **PlaylistCancion:** relaciona canciones con playlists.
- **Favorito:** almacena registros de favoritos.
- **Reproduccion:** registra reproducciones.
- **Seguidor:** representa relaciones de seguimiento.
- **Historial:** almacena información histórica de la actividad.

Los modelos se definen en `Plataforma_de_musica/models.py` y se administran mediante el ORM de Django.

## 5. Instalación del proyecto

### 5.1. Clonar el repositorio

```powershell
git clone https://github.com/Pvmeela/BackEnd-Django.git
cd BackEnd-Django
```

### 5.2. Crear el entorno virtual

```powershell
python -m venv clases
```

### 5.3. Activar el entorno virtual en PowerShell

```powershell
.\clases\Scripts\Activate.ps1
```

### 5.4. Instalar las dependencias

```powershell
pip install -r requirements.txt
```

## 6. Configuración de la base de datos

La aplicación utiliza MySQL como sistema de gestión de base de datos.

**Nombre de la base de datos:** `db_backend`
**Usuario de la aplicación:** `user_backend`

En la carpeta `sql` se incluyen tres scripts:

- `01_crear_bd.sql`: crea la base de datos.
- `02_crear_usuario.sql`: crea el usuario de MySQL.
- `03_permisos.sql`: asigna permisos sobre la base de datos.

Los scripts deben ejecutarse en ese orden con una cuenta de MySQL que tenga los permisos administrativos necesarios.

Antes de ejecutar el script de creación del usuario, se debe reemplazar la contraseña de ejemplo por una contraseña segura.

## 7. Variables de entorno

El proyecto utiliza un archivo `.env` para mantener separadas las credenciales y otras configuraciones sensibles.

Este archivo debe crearse en la carpeta principal del proyecto, junto a `manage.py`.

Debe contener las variables que utiliza `motor_django/settings.py`, incluyendo la clave secreta de Django y los datos de conexión a MySQL.

Ejemplo de referencia:

```dotenv
SECRET_KEY=REEMPLAZAR_POR_CLAVE_SEGURA
DB_NAME=db_backend
DB_USER=user_backend
DB_PASSWORD=REEMPLAZAR_POR_CONTRASENA
DB_HOST=localhost
DB_PORT=3306
```

Los nombres de las variables deben coincidir con los utilizados en `settings.py`.

**Por seguridad, el archivo `.env` real no debe subirse a GitHub.**

## 8. Migraciones

Una vez configurada la conexión a MySQL, ejecutar:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Estos comandos permiten generar y aplicar las migraciones correspondientes al modelo de datos.

## 9. Ejecutar el servidor

Iniciar el servidor de desarrollo con:

```powershell
python manage.py runserver
```

La aplicación estará disponible en:

http://127.0.0.1:8000/

## 10. API REST

La API REST está desarrollada utilizando Django REST Framework.

Se utilizan:

- `ModelSerializer` para la serialización.
- `ModelViewSet` para las operaciones CRUD.
- `DefaultRouter` para generar las rutas de los endpoints.

### Operaciones HTTP

| Método | Función |
|---|---|
| GET | Consultar registros |
| POST | Crear registros |
| PUT | Actualizar completamente |
| PATCH | Actualizar parcialmente |
| DELETE | Eliminar registros |

### Endpoints de ejemplo

| Endpoint | Descripción |
|---|---|
| `/api/generos/` | Administración de géneros |
| `/api/artistas/` | Administración de artistas |
| `/api/canciones/` | Administración de canciones |

Los demás endpoints se encuentran configurados en `Plataforma_de_musica/urls.py`.

Las operaciones disponibles dependen de los permisos asignados a cada ViewSet.

## 11. Autenticación de usuarios

El proyecto utiliza el sistema de autenticación de Django.

Se implementaron las siguientes funcionalidades:

- Registro mediante `UserCreationForm`.
- Inicio de sesión.
- Cierre de sesión.
- Control de acceso a vistas protegidas.
- Gestión de sesiones.

### Rutas de autenticación

| Ruta | Función |
|---|---|
| `/registro/` | Registro de usuarios |
| `/accounts/login/` | Inicio de sesión |
| `/accounts/logout/` | Cierre de sesión mediante formulario POST |

Los usuarios registrados mediante `UserCreationForm` pertenecen al sistema de autenticación de Django, que es independiente del modelo musical `Usuario`.

## 12. Vistas basadas en funciones y clases

### Vista basada en función (FBV)

Se implementó una vista protegida utilizando el decorador `@login_required`.

Ruta:

`/api/protegida-funcion/`

### Vista basada en clase (CBV)

Se implementó una vista protegida utilizando `LoginRequiredMixin` y `TemplateView`.

Ruta:

`/api/protegida-clase/`

Ambas vistas requieren que el usuario haya iniciado sesión para acceder al dashboard.

## 13. Control de acceso

En los ViewSets de Django REST Framework se utilizan clases de permisos como:

- `IsAuthenticated`: requiere un usuario autenticado.
- `IsAuthenticatedOrReadOnly`: permite consultas públicas y exige autenticación para modificar datos.
- `IsAdminUser`: restringe el acceso a usuarios administradores.

La configuración de permisos se encuentra en `Plataforma_de_musica/views.py`.

## 14. Administración de Django

Para crear una cuenta administradora, ejecutar:

```powershell
python manage.py createsuperuser
```

El panel administrativo está disponible en:

http://127.0.0.1:8000/admin/

## 15. Verificación del proyecto

Para comprobar la configuración general de Django:

```powershell
python manage.py check
```

Para revisar las migraciones aplicadas:

```powershell
python manage.py showmigrations
```

Para probar la API REST se pueden utilizar el navegador de Django REST Framework o herramientas como Postman.

Se recomienda comprobar las operaciones GET, POST, PUT, PATCH y DELETE, respetando los permisos y las relaciones de los modelos.

## 16. Control de versiones

El proyecto utiliza Git y GitHub para mantener un historial de los cambios realizados durante las evaluaciones.

Repositorio:

https://github.com/Pvmeela/BackEnd-Django

Los archivos sensibles, como `.env`, y el entorno virtual se excluyen del repositorio mediante `.gitignore`.

## 17. Evaluaciones

### Evaluación N.° 2

Desarrollo de una API REST con Django REST Framework, incorporando modelo de datos, persistencia en MySQL, serializers, ViewSets, rutas mediante Router y operaciones CRUD.

### Evaluación N.° 3

Continuación del proyecto anterior, incorporando autenticación, registro de usuarios, vistas basadas en funciones y clases, sesiones y mecanismos de control de acceso.

## 18. Autoría

Proyecto individual desarrollado para la asignatura Programación Backend de INACAP.

**Docente:** Erick Bailey Rebolledo.
