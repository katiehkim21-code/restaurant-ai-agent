"""API routes for the scheduling module."""

from fastapi import APIRouter

router = APIRouter(prefix="/scheduling", tags=["scheduling"])


@router.get("/health", summary="scheduling module health check")
def scheduling_health() -> dict[str, str]:
    """Return a simple health status for the scheduling module."""
    return {"module": "scheduling", "status": "ok"}
