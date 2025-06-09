# API Segura - Trabajo Práctico Final

Este repositorio contiene el código fuente del trabajo práctico final para la materia Desarrollo de Software Seguro. El proyecto consiste en una única API REST construida con **FastAPI** que integra múltiples capas y mecanismos de seguridad.

---

### Características Principales de la Entrega Final

La API implementa los siguientes mecanismos de seguridad y características:

* **Autenticación y Autorización con OAuth 2.0**: Flujo "Password Bearer" para un inicio de sesión seguro y manejo de tokens.
* **JSON Web Tokens (JWT)**: Creación y validación de tokens firmados para proteger endpoints.
* **Autenticación por API Key**: Validación de una clave secreta enviada en los encabezados HTTP (`X-API-KEY`).
* **Autenticación Básica**: Soporte para el esquema de autenticación básico estándar.
* **Filtrado por Dirección IP**: Un middleware que restringe el acceso a la API únicamente a las IPs incluidas en una lista blanca.
* **Configuración Segura**: Manejo de todos los secretos y configuraciones a través de variables de entorno, separando el código de los datos sensibles.
* **Documentación Interactiva Automática**: Generación de una interfaz de usuario con Swagger UI para probar todos los endpoints de forma interactiva.

---

### Tecnologías Utilizadas

* **Framework**: FastAPI
* **Servidor ASGI**: Uvicorn
* **Validación de Datos**: Pydantic
* **Manejo de JWT**: Python-jose
* **Hashing de Contraseñas**: Passlib
* **Variables de Entorno**: Python-dotenv

---

### Configuración y Ejecución (Entrega Final con FastAPI)

Siga estos pasos para configurar y ejecutar el proyecto final en un entorno local.

#### 1. Clonar el Repositorio

```bash
git clone [https://github.com/Santech09/APIvillalba.git](https://github.com/Santech09/APIvillalba.git)
cd APIvillalba
```

#### 2. Crear y Activar Entorno Virtual

Es fundamental trabajar dentro de un entorno virtual para aislar las dependencias del proyecto.

```bash
# Crear el entorno
python -m venv venv

# Activar en Windows
.\venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

#### 3. Instalar Dependencias

El archivo `requirements.txt` contiene todas las librerías necesarias.

```bash
pip install -r requirements.txt
```

#### 4. Configurar Variables de Entorno (Paso Crucial)

Este proyecto carga su configuración desde un archivo `.env`. Para configurarlo:

1.  Cree una copia del archivo de ejemplo `.env.example` y renómbrela a **`.env`**.
2.  Abra el nuevo archivo `.env` y rellene las variables necesarias. Para la mayoría de las pruebas locales, los valores por defecto funcionarán.

#### 5. Ejecutar la Aplicación

Una vez configurado, inicie el servidor con el siguiente comando:

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000` y la documentación interactiva en **`http://127.0.0.1:8000/docs`**.

---

### Anexo: Implementación de Flask (Entregas Anteriores)

La siguiente sección detalla la implementación y prueba de la aplicación **Flask** desarrollada en las entregas anteriores de este proyecto. Se incluye a modo de referencia histórica y para documentar la evolución del trabajo. Las instrucciones a continuación pertenecen a la carpeta `flask-app` del repositorio.

#### 1. Ejecutar la Aplicación Flask
Ir a la carpeta `flask-app/`:
```bash
cd flask-app
```

Crea y activa el entorno virtual (si no lo has hecho para esta app):
```bash
python -m venv venv
# Activar en Windows:
.\venv\Scripts\activate
# Activar en macOS/Linux:
source venv/bin/activate
```

Instala las dependencias de Flask:
```bash
pip install -r requirements.txt
```

Ejecuta la aplicación:
```bash
python app.py
```
La aplicación Flask estará disponible en `http://127.0.0.1:5000`.

#### 2. Pruebas de los Endpoints de Flask

##### API Key (Flask)
* **Endpoint**: `GET http://127.0.0.1:5000/flask/api-key`
* **Header**: `x-api-key: 12345ABC`
* **Respuesta Exitosa**:
    ```json
    { "mensaje": "Acceso con API Key concedido en Flask!" }
    ```

##### JWT – Generación de Token (Login)
* **Endpoint**: `POST http://127.0.0.1:5000/flask/login`
* **Body (JSON)**:
    ```json
    {
      "username": "admin",
      "password": "secret"
    }
    ```
* **Respuesta**: Se recibirá un token JWT.

##### JWT – Endpoint Protegido
* **Endpoint**: `GET http://127.0.0.1:5000/flask/jwt-protected`
* **Header**: `Authorization: Bearer <tu_token_JWT_obtenido>`
* **Respuesta**: Mensaje confirmando el acceso.

##### Filtrado por IP en Flask
Se configuró un middleware para restringir el acceso. Para probarlo, se puede modificar la variable `ALLOWED_IPS` en el código de `flask-app/app.py` a un valor que no sea `127.0.0.1`. Al realizar una solicitud, la API debería retornar un error `403`.