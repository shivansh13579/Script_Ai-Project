from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "Reel Script AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    DATABASE_URL: str = "mysql+pymysql://root:shivansh%40123@localhost:3306/script_generator"

    OPENAI_API_KEY: str
    TAVILY_API_KEY: str
    # NEWS_API_KEY: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()