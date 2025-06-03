from flask import Flask, request, jsonify, abort
from functools import wraps
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flasgger import Swagger

app = Flask(__name__)

# Configuración de Flasgger para Swagger / OpenAPI
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API Segura - Entrega 2",
        "description": "API que implementa autenticación por API Key, filtrado por IP y JWT.",
        "version": "2.0"
    },
    "securityDefinitions": {
        "apiKey": {
            "type": "apiKey",
            "name": "x-api-key",
            "in": "header"
        }
    }
}
swagger = Swagger(app, template=swagger_template)

# Configuración de JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Cambiar en producción
jwt = JWTManager(app)

# Claves API válidas y direcciones IP autorizadas
VALID_API_KEYS = ["12345ABC"]
ALLOWED_IPS = ["127.0.0.1"]

# Decorador para validar API Key
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if api_key and api_key in VALID_API_KEYS:
            return f(*args, **kwargs)
        abort(401)
    return decorated

# Middleware para controlar IP
@app.before_request
def limit_remote_addr():
    if request.remote_addr not in ALLOWED_IPS:
        abort(403)

@app.route('/flask/api-key', methods=['GET'])
@require_api_key
def flask_api_key():
    """
    Endpoint para autenticación mediante API Key.
    ---
    security:
      - apiKey: []
    responses:
      200:
        description: Acceso concedido.
        examples:
          application/json: { "mensaje": "Acceso con API Key concedido en Flask!" }
      401:
        description: API Key inválida.
    """
    return jsonify({"mensaje": "Acceso con API Key concedido en Flask!"})

@app.route('/flask/login', methods=['POST'])
def login():
    """
    Endpoint de login para generar un JWT.
    ---
    parameters:
      - in: body
        name: credentials
        description: Credenciales de usuario.
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Token generado exitosamente.
        examples:
          application/json: { "access_token": "<token>" }
      401:
        description: Credenciales incorrectas.
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "admin" or password != "secret":
        return jsonify({"msg": "Credenciales incorrectas"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/flask/jwt-protected', methods=['GET'])
@jwt_required()
def protected_jwt():
    """
    Endpoint protegido que requiere JWT.
    ---
    security:
      - Bearer: []
    responses:
      200:
        description: Acceso permitido con JWT válido.
        examples:
          application/json: { "mensaje": "Acceso concedido para admin mediante JWT" }
      401:
        description: Token inválido o ausente.
    """
    current_user = get_jwt_identity()
    return jsonify({"mensaje": f"Acceso concedido para {current_user} mediante JWT"})
    
if __name__ == '__main__':
    app.run(debug=True)

