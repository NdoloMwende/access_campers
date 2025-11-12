from flask import Flask
from config import Config
from models import db, migrate

# Import models so migrations detect them
from models.camper import Camper
from models.activity import Activity
from models.signup import Signup

# Import routes
from routes.campers import campers_bp
from routes.activities import activities_bp
from routes.signups import signups_bp

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
