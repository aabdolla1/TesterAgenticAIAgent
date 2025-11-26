from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://tester:tester@localhost:5432/tester_db"
    ENVIRONMENT: str = "development"
    class Config:
        env_file = ".env"

settings = Settings()
