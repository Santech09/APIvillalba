from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader, HTTPBasic, HTTPBasicCredentials
from config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

API_KEY_NAME = "X-API-KEY"
api_key_header_scheme = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

async def get_api_key(api_key_header: str = Depends(api_key_header_scheme)):
    if api_key_header not in settings.VALID_API_KEYS:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API Key inválida o ausente")
    return api_key_header

basic_auth_scheme = HTTPBasic()

async def verify_basic_credentials(credentials: HTTPBasicCredentials = Depends(basic_auth_scheme)):
    is_correct_username = credentials.username == settings.BASIC_AUTH_USERNAME
    is_correct_password = credentials.password == settings.BASIC_AUTH_PASSWORD
    if not (is_correct_username and is_correct_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas", headers={"WWW-Authenticate": "Basic"})
    return credentials.username