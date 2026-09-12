import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DEBUG = os.getenv("FLASK_DEBUG", "1") == "1"
    REDIS_URL = os.getenv("REDIS_URL", "redis://:dev_redis_password@redis:6379/0")
