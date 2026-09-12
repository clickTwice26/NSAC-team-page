from __future__ import annotations

import os
import socket
from typing import TYPE_CHECKING, Optional

import redis
from flask import current_app

if TYPE_CHECKING:
    from flask import Flask

# Standalone / global redis connection object
redis_client: Optional[redis.Redis] = None


def resolve_redis_url(url: str) -> str:
    """
    If url targets 'redis' host but we are running outside Docker containers,
    fallback to 'localhost' so local development works seamlessly.
    """
    if "@redis:" in url or "://redis:" in url:
        try:
            socket.gethostbyname("redis")
        except socket.gaierror:
            url = url.replace("@redis:", "@localhost:").replace("://redis:", "://localhost:")
    return url


def init_redis(app: Flask) -> redis.Redis:
    """Initialize Redis connection using the Flask app config."""
    global redis_client
    raw_url = app.config.get(
        "REDIS_URL",
        os.getenv("REDIS_URL", "redis://:dev_redis_password@redis:6379/0"),
    )
    redis_url = resolve_redis_url(raw_url)
    redis_client = redis.from_url(redis_url, decode_responses=True, socket_timeout=2)
    app.extensions["redis"] = redis_client
    return redis_client


def get_redis_client() -> redis.Redis:
    """
    Get the Redis client instance.
    Works inside or outside of Flask application context.
    """
    global redis_client
    if current_app and "redis" in current_app.extensions:
        return current_app.extensions["redis"]

    if redis_client is None:
        raw_url = os.getenv("REDIS_URL", "redis://:dev_redis_password@redis:6379/0")
        redis_url = resolve_redis_url(raw_url)
        redis_client = redis.from_url(redis_url, decode_responses=True, socket_timeout=2)

    return redis_client
