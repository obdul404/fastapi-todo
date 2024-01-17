# app/core/config.py
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    API_VERSION: str = "1.0.0"
    CONTACT: dict = {
        "name": "Todo",
        "url": "xyz",
        "email": "xyz",
    }
    ENV: str = "dev"
    if ENV == "dev":
        RELOAD: bool = True
        LOG_LEVEL: str = "debug"
    else:
        RELOAD: bool = False
        LOG_LEVEL: str = "info"
    
    ALLOWED_HOSTS: list = ["*"]
    
    DATABASE_URL: str
    class Config:
        env_file = "./.env"
        extra = "ignore"

settings = Settings()