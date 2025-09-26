# PFO 2 - Sistema de Gestión de Tareas con API y Base de Datos

Proyecto desarrollado para la materia Programación en Redes de la Tecnicatura en Desarrollo de Software en el ITFS 29.

Implementación de una API REST con **Flask** y pesristencia en **SQLite**.  
Incluye un **cliente en consola** que interactua con la API.

---

## Estructura del proyecto

PFO2-GarciaQuintans/  
│── templates/  
│ └── tareas.html #Página de bienvenida  
│── cliente.py # Cliente en consola  
│── database.py # Conexión y consultas a SQLite  
│── database.sqlite # Base de datos (se crea automáticamente)  
│── servidor.py # API Flask  
│── requirements.txt # Dependencias del proyecto


## Instalacion y ejecución

1. **Clonar el respositorio**

        git clone <>  
        cd PFO2-GarciaQuintans

2. **Instalar dependencias**  

        pip install -r requirements.txt

3. **Iniciar el servidor Flask**  

        flask --app servidor run

    El servidor quedará escuchando en https://localhost:5000

4. **Ejecutar el cliente en consola**  

        python cliente.py


## Usuario de Prueba

Para facilitar las pruebas, el sistema incluye un usuario ya creado:

* **Usuario:** nombre
* **Contraseña:** 1234


## Endpoints principales

1. **Registro de Usuario**

    * POST /registro
    * Cuerpo JSON:  

            {  
                "username": "nombre",  
                "password": "1234"  
            }

    * Respuesta exitosa:  

            {
                "mensaje": "Usuario creado correctamente"
            }

2. **Inicio de Sesión**

    * POST /login
    * Cuerpo JSON:

            {  
                "username": "nombre",  
                "password": "1234"  
            }

    * Respuesta Exitosa

            {
                "mensaje": "Se inicio sesion correctamente"
            }

3. **Pagina de Tareas**  

    * GET /tareas
    * Devuelve un HTML de Bienvenida

## Cliente en Consola

El archivo cliente.py permite interactuar con la API directamente desde la terminal.  

Opciones disponibles:

1. Registrarse 
2. Iniciar Sesión
3. Salir

Una vez iniciada la sesión se accede al Gestor de Tareas.

