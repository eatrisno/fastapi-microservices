from functools import cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


@cache
def settings() -> Settings:
    return Settings()