# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # The format is postgresql://user:password@host/dbname
    DATABASE_URL: str = "postgresql://postgres:amsa0406@localhost/myprojectdb"

    class Config:
        env_file = ".env"

settings = Settings()