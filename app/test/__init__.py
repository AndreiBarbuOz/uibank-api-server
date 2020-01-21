import logging

import connexion
from flask_testing import TestCase
from pymongo import MongoClient

from app.encoder import JSONEncoder
from app import init_app

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1aWJhbmsuYXp1cmV3ZWJzaXRlcy5jb20iLCJleHAiOjE1ODAxMDIyODAsInN1YiI6IjEyMzQ1Njc4OTAifQ.6IL8PuvByUH_NufaXBMGdpISFcfPNbVu0vFAF0R5ko4"
err_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1aWJhbmsuYXp1cmV3ZWJzaXRlcy5jb20iLCJleHAiOjE1ODAxMDIyODAsInN1YiI6IjEyMzQ1Njc4OTAifQ.uqVY6fh_QPM-ZOMWIWObdi1b6VvARJovYO2dF38sfa4'

class BaseTestCase(TestCase):

    def create_app(self):
        app = init_app('TEST')
        return app.app
