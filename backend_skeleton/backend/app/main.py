from fastapi import FastAPI
from app.api import projects, requirements

def create_app() -> FastAPI:
    app = FastAPI(title="Tester Agentic AI Backend", version="0.1.0")
    app.include_router(projects.router)
    app.include_router(requirements.router)
    return app

app = create_app()
