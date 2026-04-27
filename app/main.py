from fastapi import FastAPI

from app.api.routes_health import router as health_router

app = FastAPI(
    title="Industrial AI Platform",
    version="0.1.0",
    description="Portfolio project for industrial computer vision and MLOps.",
)
app.include_router(health_router)
