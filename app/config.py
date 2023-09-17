# import libraries
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


# Settings class that reads the .env file
class Settings(BaseSettings):
    app_name: str = "Disaster Management"
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_settings():
    return Settings()

