# main.py

from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from config import settings
from security import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_api_key,
    verify_basic_credentials
)
from jose import JWTError, jwt

# --- CONFIGURACIÓN INICIAL DE LA APP ---
app = FastAPI(
    title="API Segura - Entrega Final",
    description="Implementación de múltiples mecanismos de seguridad en FastAPI.",
    version="1.0.0"
)

# --- MIDDLEWARE PARA FILTRO DE IP ---
@app.middleware("http")
async def ip_filter_middleware(request: Request, call_next):
    """Filtra las peticiones entrantes por dirección IP."""
    client_ip = request.client.host
    if client_ip not in settings.ALLOWED_IPS:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail": f"Acceso denegado: La IP {client_ip} no está autorizada"}
        )
    response = await call_next(request)
    return response

# --- BASE DE DATOS SIMULADA Y LÓGICA DE OAUTH2 ---
# Simulación de una base de datos de usuarios con contraseñas hasheadas
fake_users_db = {
    "santiago": {
        "username": "santiago",
        "full_name": "Santiago Curti",
        "email": "santiago@example.com",
        "hashed_password": get_password_hash("villalba"), # Contraseña hasheada
        "disabled": False,
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Decodifica el token para obtener el usuario actual."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = fake_users_db.get(username)
    if user is None:
        raise credentials_exception
    return user

# --- ENDPOINTS DE LA API ---

@app.post("/token", tags=["OAuth2 - Autenticación"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Endpoint para que un usuario inicie sesión y obtenga un token de acceso."""
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", tags=["Rutas Protegidas"])
async def read_users_me(current_user: dict = Depends(get_current_user)):
    """Ruta protegida que devuelve la información del usuario autenticado vía OAuth2."""
    return current_user

@app.get("/data/apikey", tags=["Rutas Protegidas"])
async def get_data_apikey(api_key: str = Depends(get_api_key)):
    """Ruta protegida que requiere una API Key válida."""
    return {"mensaje": "Acceso concedido con API Key", "data": "Información sensible"}

@app.get("/data/basic", tags=["Rutas Protegidas"])
async def get_data_basic(username: str = Depends(verify_basic_credentials)):
    """Ruta protegida que requiere Autenticación Básica."""
    return {"mensaje": f"Acceso concedido para el usuario: {username}", "data": "Información sensible"}

@app.get("/", tags=["General"])
def read_root():
    """Endpoint principal de bienvenida."""
    return {"mensaje": "Bienvenido a la API Segura de Santiago"}