# Team Page

Minimal Flask project scaffold with a clean structure and password-protected Redis integration.

## Structure

- `app/` - Flask package
  - `__init__.py` - application factory & Redis initialization
  - `redis_client.py` - reusable Redis connection helper
  - `routes.py` - blueprint and routes
  - `templates/` - Jinja templates
  - `static/` - static assets
- `config.py` - application config with `.env` loader
- `run.py` - local entry point
- `Dockerfile` - production container image
- `docker-compose.yml` - orchestrated web + password-protected Redis

## Environment Variables (`.env`)

```env
SECRET_KEY=dev-secret-key-change-in-prod
FLASK_DEBUG=1
PORT=8000
REDIS_PASSWORD=dev_redis_password
REDIS_URL=redis://:dev_redis_password@redis:6379/0
```

> **Note**: If running Flask directly on your host machine while Redis runs in Docker, use `REDIS_URL=redis://:dev_redis_password@localhost:6379/0` in `.env`.

## How to use Redis anywhere in code

Import `get_redis_client`:

```python
from app.redis_client import get_redis_client

# Get client instance
r = get_redis_client()

# Standard Redis operations
r.set("user:100", "Alex")
name = r.get("user:100")
r.incr("page_views")
```

## Running with Docker Compose (Recommended)

Start both Flask and password-protected Redis:

```bash
docker compose up --build
```

Then open `http://localhost:8000` (or `http://localhost:8000/health/redis`).

## Running Locally

```bash
# 1. Start Redis only (if using docker for redis)
docker compose up -d redis

# 2. Setup virtual environment & run Flask
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```
