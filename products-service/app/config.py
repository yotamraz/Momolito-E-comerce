from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    service_name: str = "products-service"
    service_port: int = 8002
    database_url: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
