# app/utils/errors.py
from fastapi.responses import JSONResponse

def structured_error(message: str, code: int = 400):
    return JSONResponse(status_code=code, content={"error": message})
