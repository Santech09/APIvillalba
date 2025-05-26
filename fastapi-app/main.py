from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

app = FastAPI(
    title="API Segura con FastAPI",
    description="Ejemplo de autenticación básica con FastAPI y documentación automática OpenAPI",
    version="1.0.0"
)

security = HTTPBasic()

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    # Verifica que el usuario y la contraseña coincidan con lo esperado
    if not (secrets.compare_digest(credentials.username, "admin") and secrets.compare_digest(credentials.password, "secret")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/api/protegida", tags=["Protegida"])
def protected_endpoint(user: str = Depends(verify_credentials)):
    return {"mensaje": f"Acceso concedido a {user}!"}
