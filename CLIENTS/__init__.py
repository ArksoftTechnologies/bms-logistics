from flask import Flask
from flask_login import LoginManager
import os


# Globally accessible libraries
# login_manager = LoginManager()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    # login_manager.init_app(app)


    with app.app_context():
        # Include our Routes
        from .HOME.routes import home_bp
        from .AUTH.routes import auth_bp

        # Register Blueprints
        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp, url_prefix="/auth")

        return app