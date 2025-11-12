from flask import Flask
import os,sys
# Ensure the parent directory is in the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.config import Config
from server.models import db, migrate
from server.models.camper import Camper
from server.models.activity import Activity
from server.models.signup import Signup
from server.routes.campers import campers_bp
from server.routes.activities import activities_bp
from server.routes.signups import signups_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(campers_bp)
    app.register_blueprint(activities_bp)
    app.register_blueprint(signups_bp)

    @app.route("/")
    def index():
        return {
            "message": "Welcome to the Camp API!",
            "available_endpoints": [
                "/campers",
                "/activities",
                "/signups"
            ]
        }

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5555, debug=True)
