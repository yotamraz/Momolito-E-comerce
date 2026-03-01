from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    service_name: str = "users-service"
    service_port: int = 8001
    database_url: str = ""

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
