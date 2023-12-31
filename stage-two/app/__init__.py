"""
    Script Initialise the app and all it dependecys
"""
from .configs import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config=Config):
    """ Application Factory """
    app = Flask(__name__)
    app.config.from_object(config)
    
    from app.api import bp as api_bp
    app.register_blueprint(blueprint=api_bp, url_prefix="/api")

    db.init_app(app)
    migrate.init_app(app, db)
    return app

from . import models
