from flask import Flask

from .redis_client import init_redis
from .routes import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize Redis extension
    init_redis(app)

    # Register Blueprints
    app.register_blueprint(main_bp)

    return app
