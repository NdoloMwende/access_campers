from flask import Flask
from server.config import Config
from server.models import db, migrate

# Import models so migrations detect them
from server.models.camper import Camper
from server.models.activity import Activity
from server.models.signup import Signup

# Import routes
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

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5555, debug=True)
