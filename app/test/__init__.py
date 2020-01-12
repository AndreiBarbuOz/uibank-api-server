import logging

import connexion
from flask_testing import TestCase

from app.encoder import JSONEncoder
from app.__main__ import client

import mockupdb
from pymongo import MongoClient

server = mockupdb.MockupDB()
port = server.run()
client = MongoClient(server.uri)

class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        app.app.config['TESTING']= True
        return app.app
