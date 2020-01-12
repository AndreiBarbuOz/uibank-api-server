import os
import connexion
from pymongo import MongoClient
from app import encoder

client = MongoClient(os.environ['MONGO_DB_STRING'])

#app = connexion.App(__name__, specification_dir='./swagger/')
#app.app.json_encoder = encoder.JSONEncoder
#app.add_api('swagger.yaml', arguments={'title': 'UiBank'}, pythonic_params=True)
#
#
if __name__ == "__main__":
    print(client)
    db = client['uibank']
    print(db)
    col = db['Customer']
    print(col)
    print(db.list_collection_names())
#    # Only for debugging while developing
#    app.run(host="0.0.0.0", debug=True, port=80)
#
