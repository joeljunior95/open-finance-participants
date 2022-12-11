from flask import Flask, g
from flask_cors import CORS
from pymongo import MongoClient

def create_app():
    app = Flask('open-finance-participants', 
                template_folder='src/application/templates',
                static_folder='src/application/static')

    CORS(app)

    app.config.from_object('src.config.Config')
    with app.app_context():
        from src.participant import participant_routes

        app.register_blueprint(participant_routes.participant_bp)
        
        client = MongoClient(app.config['DATABASE_URI'])
        try:
            client.server_info()
        except Exception as e:
            raise Exception('Could not connect to MongoDB server')
        
        app.db = client[app.config['DATABASE_NAME']]

    return app