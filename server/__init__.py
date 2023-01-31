from flask import Flask
from flask_cors import CORS
import os


def init_app():
    """Initialize the core application."""
    template_dir = os.path.join(os.environ["APP_PATH"], "server", "client", "templates")
    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder=template_dir,
        static_url_path='',
        static_folder=template_dir,
    )
    app.config.from_object('config.Config')
    CORS(app)
    with app.app_context():
        # Register Blueprints
        from server.client.routes import client_blueprint
        from server.api.routes import api_blueprint

        app.register_blueprint(client_blueprint)
        app.register_blueprint(api_blueprint)

        return app
