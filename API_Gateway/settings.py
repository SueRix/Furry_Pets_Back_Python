import os


class Settings:
    # AUTH_SERVICE_URL: str = os.getenv('AUTH_SERVICE_URL', 'http://djangoapp:8002')
    AUTH_SERVICE_URL: str = os.getenv('AUTH_SERVICE_URL', 'http://127.0.0.1:8080')
    CALENDAR_SERVICE_URL: str = os.getenv('CALENDAR_SERVICE_URL', 'http://5000')
    class Config:
        env_file = ".env"


settings = Settings()
