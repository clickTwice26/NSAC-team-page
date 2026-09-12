# Team Page

Minimal Flask project scaffold with a clean structure.

## Structure

- `app/` - Flask package
  - `__init__.py` - application factory
  - `routes.py` - blueprint and routes
  - `templates/` - Jinja templates
  - `static/` - static assets
- `config.py` - application config
- `run.py` - local entry point

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Then open `http://127.0.0.1:5000`.

## Run with Docker

```bash
docker build -t team-page .
docker run --rm -p 8000:8000 team-page
```

The app listens on port `8000` inside the container, which is friendly for most Docker-based deploy providers.
