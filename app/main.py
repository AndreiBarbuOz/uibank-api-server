import os
import connexion
from pymongo import MongoClient
from app import encoder
from app import db

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'UiBank'}, pythonic_params=True, validate_responses=True)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
