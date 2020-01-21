"""Flask config class."""
import os


class Config:
    """Base config vars."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    DEBUG = False
    TESTING = False


class ProdConfig(Config):
    MONGO_DB_STRING = os.environ.get('MONGO_DB_STRING')
    JWT_SECRET = os.environ.get('JWT_SECRET')


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    MONGO_DB_STRING = os.environ.get('MONGO_DB_STRING')
    JWT_SECRET = 'testing'