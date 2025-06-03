# APIVillalba Entrega 2

Este repositorio contiene la implementación práctica de mecanismos avanzados de autenticación y seguridad, desarrollados en Flask y FastAPI. Se incluyen dos aplicaciones:

Flask: que implementa autenticación por API Key, generación y validación de JWT, y filtrado por IP.

FastAPI: que integra autenticación por API Key, filtrado por IP (mediante middleware) y documentación interactiva con OpenAPI (Swagger UI).

## Contenido del Repositorio

- **flask-app/**: Implementación de autenticación básica en Flask, usando Flask-HTTPAuth.
- **fastapi-app/**: Implementación de autenticación básica en FastAPI, con generación automática de documentación OpenAPI.
- **LICENSE**: Archivo de licencia.
- **README.md**: Este documento.

## Requisitos Técnicos

- Python 3.7 o superior.
- Virtualenv (o similar) para gestionar entornos virtuales.

## Instrucciones de Uso
```bash

### 1. Clonar el Repositorio

   git clone https://github.com/tuusuario/APIVillalba-Entrega1.git
   cd APIVillalba-Entrega1

### 2. Ejecutar la Aplicación Flask
Ir a la carpeta flask-app/:
   cd flask-app

Crea y activa el entorno virtual:
   python -m venv venv
   source venv/Scripts/activate

Instala las dependencias:
   pip install -r requirements.txt

Ejecuta la aplicación:
   python app.py

API Key (Flask): Realizar una solicitud GET al endpoint:

http://127.0.0.1:5000/flask/api-key
Incluir en los headers: x-api-key: 12345ABC
Con la API Key correcta, se obtendrá el siguiente JSON de respuesta:

json
{ "mensaje": "Acceso con API Key concedido en Flask!" }

JWT – Generación de Token (Login): Realizar una solicitud POST al endpoint de login:

http://127.0.0.1:5000/flask/login
En el cuerpo de la solicitud (formato JSON), enviar las credenciales:

json
{
  "username": "admin",
  "password": "secret"
}
Se recibirá un token JWT en la respuesta.

JWT – Endpoint Protegido: Utilizar el token recibido para acceder al endpoint protegido mediante JWT:

http://127.0.0.1:5000/flask/jwt-protected
Incluir en los headers: Authorization: Bearer <tu_token_JWT>

La respuesta deberá confirmar el acceso correcto (por ejemplo, un mensaje de éxito).

Filtrado por IP en Flask: Se ha configurado un middleware para restringir el acceso según la IP. Para probarlo, se puede modificar temporalmente la variable ALLOWED_IPS en el código (por ejemplo, cambiándola a ["192.168.1.100"]) y realizar una solicitud desde 127.0.0.1, la cual debería retornar un error 403 con el mensaje:

json
{ "detail": "Acceso denegado: IP no autorizada" }

### 3. Ejecutar la Aplicación FastAPI
Ir a la carpeta fastapi-app/:
   cd ../fastapi-app

Crea y activa el entorno virtual:
   python -m venv venv
   source venv/Scripts/activate

Instala las dependencias:
   pip install -r requirements.txt

Ejecuta la aplicación:
   uvicorn main:app --reload

Accede a la documentación interactiva en tu navegador: http://127.0.0.1:8000/docs Prueba el endpoint protegido en Swagger UI ingresando las siguientes credenciales:
Importante, cuando ingresas al link y da error, revisar si se intento conectar por https en lugar de http

Endpoint de API Key (FastAPI):

Realizar una solicitud GET al endpoint:

http://127.0.0.1:8000/fastapi/api-key
Incluir en los headers: x-api-key: 12345ABC

Con la clave válida, se obtendrá una respuesta en JSON similar a:
{ "mensaje": "Acceso con API Key concedido en FastAPI!" }

Filtrado por IP en FastAPI: La aplicación incluye un middleware que restringe el acceso basándose en la IP del cliente. Para simular un acceso no autorizado, modifica en el archivo main.py la variable ALLOWED_IPS (por ejemplo, reemplázala por ["192.168.1.100"]) y vuelve a ejecutar la aplicación. Al intentar acceder al endpoint desde 127.0.0.1, se debería retornar un error 403 con el mensaje:

{ "detail": "Acceso denegado: IP no autorizada" }
