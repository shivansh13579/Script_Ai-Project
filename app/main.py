from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.routes.health import router as health
from app.api.routes.script import router as script_router
from app.api.routes.history import router as history_router
from app.db.database import init_db_with_retry
from app.core.config import settings
from app.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    init_db_with_retry()
    logger.info("App is ready")
    yield
    logger.info("Shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health, prefix="/api/v1/health")
app.include_router(script_router, prefix="/api/v1/script", tags=["Script"])
app.include_router(history_router, prefix="/api/v1/history", tags=["History"])

@app.get("/")
def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
         "docs": "/docs"
    }

@app.get("/version")
def version():
    return {
        "version": "2.0"
    }

