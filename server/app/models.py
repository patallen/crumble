from app import db
from time import time


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.BigInteger, default=time)
    created = db.Column(db.BigInteger, default=time, onupdate=time)
