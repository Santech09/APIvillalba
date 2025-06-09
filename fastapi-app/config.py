import os
from dotenv import load_dotenv

# Carga las variables del archivo .env en el entorno actual
load_dotenv()

class Settings:
    # --- JWT Settings ---
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # --- Basic Auth Credentials ---
    BASIC_AUTH_USERNAME: str = os.getenv("BASIC_AUTH_USERNAME")
    BASIC_AUTH_PASSWORD: str = os.getenv("BASIC_AUTH_PASSWORD")

    # --- IP Filter Settings ---
    # Lee la variable como un string y la convierte en una lista de strings
    ALLOWED_IPS: list[str] = os.getenv("ALLOWED_IPS", "127.0.0.1").split(',')

    # --- API Key Settings ---
    VALID_API_KEYS: list[str] = os.getenv("VALID_API_KEYS").split(',')

# Se crea una instancia de la configuración para ser importada en otros módulos
settings = Settings()