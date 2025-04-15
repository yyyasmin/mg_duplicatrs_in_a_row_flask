
import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
from flask_cors import CORS

db = SQLAlchemy()

#FROM https://github.com/miguelgrinberg/microblog/blob/v0.15/app/__init__.py	
def create_app(config_class=Config):
    app = Flask(__name__)        
    app.config.from_object(config_class)        
    db.init_app(app)
    migrate = Migrate(app, db)

    
    #CORS(app)
    CORS(app, origins="*")

    print("\n - ÏN create_app -- app: ", app)
    
    from app.orders import ord
    #app.register_blueprint(ord)
    app.register_blueprint(ord, url_prefix='/orders')

    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app

from app import models
from app.models import *
from app import *