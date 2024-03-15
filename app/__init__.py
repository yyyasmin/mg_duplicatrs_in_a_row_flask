
import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS

db = SQLAlchemy()

#FROM https://github.com/miguelgrinberg/microblog/blob/v0.15/app/__init__.py	
def create_app(config_class=Config):
    app = Flask(__name__)        
    app.config.from_object(config_class)        
    db.init_app(app)
    CORS().init_app(app, resources={r"/submit_order": {"origins": "http://localhost:3000/"}})
	
    return app

from app import models
from app.models import *
from app import *