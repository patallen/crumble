from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

from app.views.admin import bp as admin
from app.views.public import bp as public

app.register_blueprint(public, url_prefix='/public')
app.register_blueprint(admin, url_prefix='/admin')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type,Authorization'
    )
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
