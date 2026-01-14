# Sistema de Reserva de Servicios Comunitarios

Este proyecto es una aplicación web desarrollada en Python y Flask para la gestión de reservas de instalaciones en un complejo residencial (Gimnasio, Piscina y Sauna). El sistema permite a los residentes reservar horarios garantizando el cumplimiento del aforo máximo permitido (medida COVID-19).

## 📋 Características Principales

* **Autenticación de Usuarios:** Sistema de inicio de sesión (`Login`) para residentes pre-registrados.
* **Gestión de Reservas:** Los usuarios pueden reservar servicios eligiendo fecha y hora.
* **Control de Aforo (Lógica Crítica):** El sistema verifica automáticamente si hay plazas disponibles antes de confirmar una reserva. Si el aforo está completo (`max_capacity`), la reserva es rechazada.
* **Dashboard Personal:** Visualización de las reservas activas del usuario.
* **Persistencia de Datos:** Uso de base de datos SQLite con SQLAlchemy.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.13
* **Framework Web:** Flask
* **ORM:** Flask-SQLAlchemy
* **Autenticación:** Flask-Login
* **Base de Datos:** SQLite
* **Frontend:** HTML5, Jinja2 y CSS3 (Estilos personalizados en `static/css/style.css`).

## 🚀 Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1.  **Requisitos Previos:** Tener Python instalado.

2.  **Instalar Dependencias:**
    Abre una terminal en la carpeta del proyecto y ejecuta:
    ```bash
    pip install flask flask-sqlalchemy flask-login
    ```

3.  **Ejecutar la Aplicación:**
    ```bash
    python app.py
    ```

4.  **Acceder al Sistema:**
    Abre tu navegador web y visita: `http://127.0.0.1:5000`

> **Nota:** Al ejecutar la aplicación por primera vez, el sistema creará automáticamente la base de datos `reservas.db` y cargará los datos de prueba (usuarios y servicios) mediante la función `seed_data()`.

## 🔑 Usuarios de Prueba (Credenciales)

El sistema cuenta con usuarios pre-cargados para realizar pruebas. Puedes utilizar cualquiera de los siguientes:

| Usuario | Contraseña |
| :--- | :--- |
| **residente1** | `a123456789` |
| **residente2** | `b123456789` |
| **residente3** | `c123456789` |
| **residente4** | `d123456789` |

## 📂 Estructura del Proyecto

```text
OrdinariaGuillermoGarciaPeyrona/
│
├── app.py                # Controlador principal y lógica de negocio
├── models.py             # Modelos de base de datos (User, Service, Reservation)
├── requirements.txt      # (Opcional) Lista de librerías
│
├── static/
│   └── css/
│       └── style.css     # Hoja de estilos principal
│
├── templates/            # Vistas HTML (Jinja2)
│   ├── base.html         # Plantilla base
│   ├── login.html        # Página de acceso
│   ├── dashboard.html    # Panel principal (Mis reservas)
│   └── book.html         # Formulario de reserva
│
└── instance/
    └── reservas.db       # Base de datos SQLite (se genera automáticamente)
```
## ⚙️ Reglas de Negocio (Capacidades)
Las capacidades máximas configuradas por defecto para los servicios son:

- 🏋️ Gimnasio: 2 personas

- 🏊 Piscina: 5 personas

-  Sauna: 1 persona

Autor: Guillermo García Peyrona Asignatura: Programación Concurrente / Desarrollo Web
