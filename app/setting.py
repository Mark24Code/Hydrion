import os

BASEDIR = os.path.abspath(os.path.dirname(__name__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'
    HOST = '0.0.0.0'
    PORT = 5000


class Development(Config):
    DEBUG = True
    DATABASE_URL = os.environ.get('DATABASE_URL') or os.path.join(BASEDIR, 'dev.sqlite')


class Testing(Config):
    TESTING = True
    DATABASE_URL = os.environ.get('DATABASE_URL') or os.path.join(BASEDIR, 'test.sqlite')


class Production(Config):
    DEBUG = False
    DATABASE_URL = os.environ.get('DATABASE_URL') or os.path.join(BASEDIR, 'data.sqlite')


config = {
    "development": Development,
    "testing": Testing,
    "production": Production,
    "default": Development
}
