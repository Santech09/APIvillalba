# APIVillalba Entrega 1

Este repositorio contiene la implementación y documentación de la primera entrega del trabajo práctico, enfocado en la autenticación en APIs utilizando Flask y FastAPI.

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

Accede al endpoint en tu navegador: http://127.0.0.1:5000/api/protegida e Ingresa las credenciales:
Importante, cuando ingresas al link y da error, revisar si se intento conectar por https en lugar de http

Usuario: admin
Contraseña: secret

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

Usuario: admin
Contraseña: secret
