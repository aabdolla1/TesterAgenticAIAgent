from fastapi import APIRouter

router = APIRouter(prefix="/requirements", tags=["Requirements"])

@router.get("/health")
async def requirements_health():
    return {"status": "ok", "component": "requirements-service"}
