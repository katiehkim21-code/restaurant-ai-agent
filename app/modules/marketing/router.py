"""API routes for the marketing module."""

from fastapi import APIRouter

router = APIRouter(prefix="/marketing", tags=["marketing"])


@router.get("/health", summary="marketing module health check")
def marketing_health() -> dict[str, str]:
    """Return a simple health status for the marketing module."""
    return {"module": "marketing", "status": "ok"}
