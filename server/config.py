import os

home_dir = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:////{}/crumble.db'.format(home_dir)
DEBUG = True
