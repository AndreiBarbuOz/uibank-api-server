import logging

import connexion
from flask_testing import TestCase

from app.encoder import JSONEncoder

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1aWJhbmsuYXp1cmV3ZWJzaXRlcy5jb20iLCJleHAiOjE1ODAxMDIyODAsInN1YiI6IjEyMzQ1Njc4OTAifQ.MJX5gZuBlYCkzhu6Itz32wv6-l1SzshE88UyEBvIM40"


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml', validate_responses=True, pythonic_params=True)
        return app.app
#