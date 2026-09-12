from __future__ import annotations

import os
from typing import TYPE_CHECKING, Optional

import redis
from flask import current_app

if TYPE_CHECKING:
    from flask import Flask

# Standalone / global redis connection object
redis_client: Optional[redis.Redis] = None


def init_redis(app: Flask) -> redis.Redis:
    """Initialize Redis connection using the Flask app config."""
    global redis_client
    redis_url = app.config.get(
        "REDIS_URL",
        os.getenv("REDIS_URL", "redis://:dev_redis_password@redis:6379/0"),
    )
    redis_client = redis.from_url(redis_url, decode_responses=True)
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
        redis_url = os.getenv("REDIS_URL", "redis://:dev_redis_password@localhost:6379/0")
        redis_client = redis.from_url(redis_url, decode_responses=True)

    return redis_client
