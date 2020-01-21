import os
from pymongo import MongoClient
import connexion
from app import encoder
from app import config
import logging

from app.encoder import JSONEncoder
from connexion.apps.flask_app import flask

class MongoDb(object):

    def __init__(self): 
        self.db = None

    def init_app(self, app): 
        client = MongoClient(app.config['MONGO_DB_STRING'])
        self.db = client['uibank']
    
    def get_db(self):
        if self.db is None:
            raise Exception
        return self.db

mongo_db = MongoDb()

def get_db():
    ret = mongo_db.get_db()
    print(id(ret))
    return ret

def init_app(env):
    if env == 'PROD':
        app = connexion.App(__name__, specification_dir='./swagger/')
        app.app.json_encoder = encoder.JSONEncoder
        app.add_api('swagger.yaml', arguments={
                    'title': 'UiBank'}, pythonic_params=True, validate_responses=True)
        app.app.config.from_object(config.ProdConfig)
    else: 
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='./swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml', validate_responses=True, pythonic_params=True)
        app.app.config.from_object(config.TestConfig)
    mongo_db.init_app(app.app)
    return app



__all__= ["init_app", "get_db"]
