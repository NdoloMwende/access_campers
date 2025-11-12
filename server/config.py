import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///app.db") # Default to SQLite if no env variable is set
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications to save resources
