"""API routes for the inventory module."""

from fastapi import APIRouter

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("/health", summary="inventory module health check")
def inventory_health() -> dict[str, str]:
    """Return a simple health status for the inventory module."""
    return {"module": "inventory", "status": "ok"}
