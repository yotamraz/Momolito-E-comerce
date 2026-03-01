from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    service_name: str = "orders-service"
    service_port: int = 8003
    database_url: str = ""
    users_service_url: str = "http://users-service:8001"
    products_service_url: str = "http://products-service:8002"

    class Config:
        env_file = ".env"


settings = Settings()
