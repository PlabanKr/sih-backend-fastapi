# import libraries
from pydantic_settings import BaseSettings, SettingsConfigDict

# Settings class that reads the .env file
class Settings(BaseSettings):
    app_name: str = "Disaster Management"
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")
