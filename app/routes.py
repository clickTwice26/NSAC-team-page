from flask import Blueprint, jsonify, render_template

from .redis_client import get_redis_client

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    r = get_redis_client()
    try:
        visits = r.incr("page_views")
        redis_status = f"Connected (page views: {visits})"
    except Exception as exc:
        visits = None
        redis_status = f"Unavailable ({exc})"

    return render_template("index.html", redis_status=redis_status, visits=visits)


@main_bp.route("/health/redis")
def redis_health():
    r = get_redis_client()
    try:
        is_alive = r.ping()
        return jsonify({"status": "ok", "redis_ping": is_alive})
    except Exception as exc:
        return jsonify({"status": "error", "message": str(exc)}), 500
