from sqlalchemy.ext.asyncio import AsyncSession
from app.models.project import Project

async def create_project(db: AsyncSession, name: str, description: str | None):
    project = Project(name=name, description=description)
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project
