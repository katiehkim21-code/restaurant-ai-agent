"""API routes for the reservations module."""

from fastapi import APIRouter

router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.get("/health", summary="reservations module health check")
def reservations_health() -> dict[str, str]:
    """Return a simple health status for the reservations module."""
    return {"module": "reservations", "status": "ok"}
