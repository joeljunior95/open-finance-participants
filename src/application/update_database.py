from pymongo import MongoClient
import requests
from datetime import datetime
from src.application import db


def start():
    """
    Main function.
    """
    API_LINK = "https://data.directory.openbankingbrasil.org.br/participants"
    try:
        client = db.connect()
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


