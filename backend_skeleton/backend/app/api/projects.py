from fastapi import APIRouter

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/health")
async def health_check():
    return {"status": "ok", "component": "project-service"}
