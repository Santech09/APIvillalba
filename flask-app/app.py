from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
import secrets
from flasgger import Swagger

# Configuración de Swagger con definiciones de seguridad
template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Ejemplo",
        "description": "Esta API implementa autenticación básica utilizando Flask y Flasgger.",
        "version": "1.0"
    },
    "securityDefinitions": {
        "basicAuth": {
            "type": "basic"
        }
    }
}

app = Flask(__name__)
swagger = Swagger(app, template=template)
auth = HTTPBasicAuth()

# Diccionario de usuarios de ejemplo
usuarios = {
    "admin": "secret"
}

@auth.verify_password
def verify_password(username, password):
    if username in usuarios and secrets.compare_digest(usuarios.get(username), password):
        return username
    return None

@app.route('/api/protegida', methods=['GET'])
@auth.login_required
def api_protegida():
    """
    Endpoint protegido que requiere autenticación básica.
    ---
    security:
      - basicAuth: []
    responses:
      200:
        description: Acceso concedido exitosamente.
        examples:
          application/json:
            mensaje: "Acceso concedido a admin!"
      401:
        description: Credenciales inválidas.
    """
    return jsonify({"mensaje": f"Acceso concedido a {auth.current_user()}!"})

if __name__ == '__main__':
    app.run(debug=True)
