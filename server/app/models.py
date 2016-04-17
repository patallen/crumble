from app import db
from time import time


class BaseMixin(object):
    created = db.Column(db.BigInteger, default=time)
    updated = db.Column(db.BigInteger, default=time, onupdate=time)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            raise

    def to_dict(self, exclude=None, include=None):
        include = include or []
        exclude = exclude or []
        if not isinstance(include, list):
            include = [include]
        if not isinstance(exclude, list):
            exclude = [exclude]

        cols = [k.key for k in self.__table__.columns if k.key[0] is not '_']
        attrs = [c for c in cols if c not in exclude] + include

        rv = {}
        for attr in attrs:
            if hasattr(self, attr):
                rv[attr] = unicode(getattr(self, attr))
        return rv

    def update_attributes(self, data):
        for k, v in data.iteritems():
            if hasattr(self, k):
                setattr(self, k, v)
            else:
                raise ValueError


class Document(BaseMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False, unique=True)
    body = db.Column(db.Text)
