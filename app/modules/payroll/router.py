"""API routes for the payroll module."""

from fastapi import APIRouter

router = APIRouter(prefix="/payroll", tags=["payroll"])


@router.get("/health", summary="payroll module health check")
def payroll_health() -> dict[str, str]:
    """Return a simple health status for the payroll module."""
    return {"module": "payroll", "status": "ok"}
