import os


class Settings:
    POSTGRES_SERVICE = os.getenv('POSTGRES_SERVICE')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')


settings = Settings()