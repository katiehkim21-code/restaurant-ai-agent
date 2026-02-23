"""FastAPI application entry point."""

from fastapi import FastAPI

from app.core.config import settings
from app.modules.inventory.router import router as inventory_router
from app.modules.marketing.router import router as marketing_router
from app.modules.payroll.router import router as payroll_router
from app.modules.reservations.router import router as reservations_router
from app.modules.scheduling.router import router as scheduling_router

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    description="Modular backend-first AI platform for restaurant operations.",
)


@app.get("/health", tags=["system"], summary="Application health check")
def health() -> dict[str, str]:
    """Return a simple health status for the API."""
    return {"status": "ok"}


app.include_router(reservations_router)
app.include_router(inventory_router)
app.include_router(payroll_router)
app.include_router(scheduling_router)
app.include_router(marketing_router)
