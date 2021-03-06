from time import time

from sqlalchemy.orm import validates
from werkzeug.security import (
    generate_password_hash, check_password_hash
)

from app import db
import lib.encrypt


class BaseMixin(object):
    created = db.Column(db.BigInteger, default=time)
    updated = db.Column(db.BigInteger, default=time, onupdate=time)
    default_includes = []
    default_excludes = []

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
        include.extend(self.default_includes)
        exclude.extend(self.default_excludes)

        if not isinstance(include, list):
            include = [include]
        if not isinstance(exclude, list):
            exclude = [exclude]

        cols = [k.key for k in self.__table__.columns if k.key[0] is not '_']
        attrs = [c for c in cols if c not in exclude] + include
        print "ATTRS", attrs
        rv = {}
        for attr in attrs:
            print "ATTR", attr
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
    _title = db.Column(
        db.String(256),
        nullable=False,
        unique=True,
        server_default="Untitled",
        default="Untitled"
    )
    _body = db.Column(db.Text)
    default_includes = ['title', 'body']

    @property
    def title(self):
        return lib.encrypt.decrypt(self._title)

    @title.setter
    def title(self, string):
        self._title = lib.encrypt.encrypt(string)

    @property
    def body(self):
        return lib.encrypt.decrypt(self._body)

    @body.setter
    def body(self, string):
        self._body = lib.encrypt.encrypt(string)


class Action(BaseMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action_type = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text)
    ip_address = db.Column(db.String, nullable=True)
    data = db.Column(db.Text, nullable=True)

    @classmethod
    def create(
        cls,
        action_type,
        ip_address,
        description=None,
        data=None
    ):
        cls(
            action_type=action_type,
            ip_address=ip_address,
            description=description,
            data=data
        )
        cls.save()

    @validates('action_type')
    def validate_action_type(self, action_type):
        assert action_type in self.action_types
        return action_type

    @property
    def action_types(self):
        return [
            'create_document',
            'update_document'
        ]


class Admin(BaseMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    _password = db.Column(db.Text, nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def authenticate(self, password):
        return check_password_hash(self._password, password)
