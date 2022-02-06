from functools import cache
from typing import Any, Dict, Optional

from pydantic import BaseSettings, EmailStr, SecretStr, validator

class Settings(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
    
    ENV: str = "dev"
    PROJECT_NAME: str = 'API Project'
    POSTGRES_DB: str = 'api_project'
    POSTGRES_HOST: str = 'localhost'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: SecretStr = ''
    POSTGRES_URI: Optional[str] = None

    @validator("POSTGRES_URI", pre=True)
    def validate_postgres_conn(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        password: SecretStr = values.get("POSTGRES_PASSWORD", SecretStr(""))
        return "{scheme}://{user}:{password}@{host}/{db}".format(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=password.get_secret_value(),
            host=values.get("POSTGRES_HOST"),
            db=values.get("POSTGRES_DB"),
        )

    FIRST_USER_EMAIL: EmailStr = 'admin@mail.com'
    FIRST_USER_PASSWORD: SecretStr = 'password'
    SECRET_KEY: SecretStr = 'secret'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REDIS_HOST: str = '127.0.0.1'
    REDIS_PORT: int = '6379'
    MAX_JOBS: int = 10
    ACTIVE_SERVICES: str = 'all'
    
@cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()