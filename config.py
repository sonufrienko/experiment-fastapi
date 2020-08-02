from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = "8000"


settings = Settings()

