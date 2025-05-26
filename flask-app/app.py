from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
import secrets

app = Flask(__name__)
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
    return jsonify({"mensaje": f"Acceso concedido a {auth.current_user()}!"})

if __name__ == '__main__':
    app.run(debug=True)
