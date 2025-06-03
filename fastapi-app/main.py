from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

# Claves API válidas y direcciones IP autorizadas
VALID_API_KEYS = ["12345ABC"]
ALLOWED_IPS = ["127.0.0.1"]

@app.get("/fastapi/api-key", tags=["API Key"])
def fastapi_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != "12345ABC":
        raise HTTPException(status_code=401, detail="API Key inválida")
    return {"mensaje": "Acceso con API Key concedido en FastAPI!"}

@app.middleware("http")
async def ip_filter(request: Request, call_next):
    client_ip = request.client.host
    if client_ip not in ALLOWED_IPS:
        return JSONResponse(status_code=403, content={"detail": "Acceso denegado: IP no autorizada"})
    return await call_next(request)
