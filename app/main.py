from fastapi import FastAPI

from app.api.routes import compute, health, tasks

app = FastAPI(
    title="Pure Agent API",
    version="1.0.0",
)

app.include_router(health.router)
app.include_router(tasks.router, prefix="/v1")
app.include_router(compute.router, prefix="/v1")
