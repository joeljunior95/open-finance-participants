from datetime import datetime
import os
import time

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from apscheduler.schedulers.background import BackgroundScheduler

from src.db import get_db, update_database


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_database, 'interval', minutes=30)
    scheduler.start()

def create_app():
    """Create and configure an instance of the Flask application."""
    start_scheduler()
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        # DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
        CORS_HEADERS="Content-Type"
    )

    @app.route("/")
    def hello():
        time.sleep(5)
        return jsonify({'data':'hello broda!'})
    
    @app.route("/all")
    @cross_origin()
    def all():
        cursor = get_db().openfinance.participants.find({},
            {'_id':0,'OrganisationId':1,'OrganisationName':1,'LegalEntityName':1,
            'AuthorisationServers.CustomerFriendlyLogoUri':1, 'AuthorisationServers.CustomerFriendlyName':1, 
            'AuthorisationServers.OpenIDDiscoveryDocument':1}
        )
        participants = list(cursor)
        return jsonify(participants)

    @app.route("/one", methods=['GET'])
    def one():
        time.sleep(5)

    # register the database commands
    

    return app