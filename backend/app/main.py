from fastapi import FastAPI

from app.api.v1.router import router as api_router

app = FastAPI(
    title="TalentOS API",
    version="0.1.0",
)

app.include_router(api_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "Welcome to TalentOS API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "talentos-backend",
    }