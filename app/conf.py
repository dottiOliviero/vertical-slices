from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    class Config:
        env_file = ".env"


settings = Settings()