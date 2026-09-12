from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from .redis_client import init_redis
from .routes import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Enable ProxyFix to correctly handle HTTPS, client IPs, and headers from reverse proxies
    app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=1,
        x_proto=1,
        x_host=1,
        x_prefix=1,
    )

    # Initialize Redis extension
    init_redis(app)

    # Register Blueprints
    app.register_blueprint(main_bp)

    return app
