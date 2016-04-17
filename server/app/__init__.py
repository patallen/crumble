from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

from app.views import public
app.register_blueprint(public, url_prefix='/public')
