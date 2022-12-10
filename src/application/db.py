from flask import current_app
from flask import g
from pymongo import MongoClient
import requests
from datetime import datetime

def connect():
    URI = "mongodb+srv://platform:platform@cluster0.rjiwmwb.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(URI)
    return client

def get_db():
    if "db" not in g:
        g.db = connect()

    return g.db

def update_database():
    API_LINK = "https://data.directory.openbankingbrasil.org.br/participants"
    try:
        client = connect()
        r = requests.get(API_LINK)
        data = r.json()

        client.openfinance.participants.delete_many({})
        client.openfinance.participants.insert_many(data)
        client.openfinance.upd_history.insert_one({'date':datetime.now()})

        print("MongoDB updated successfully!")
        
        return True
    except Exception:
        print("Error while downloading data and updating MongoDB")

    return False    