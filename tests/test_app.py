import pytest
from flask import Flask
import requests

from src import create_app
from src.participant.participant_model import Participant

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    yield app.test_client()

def test_status_code(client):
    rv = client.get('/participants/list')
    assert rv.status_code == 200

def test_api():
    app = create_app()
    r = requests.get(app.config['API_OPENBANKING'])
    assert r.status_code == 200
    
    raw_data = r.json()
    assert len(raw_data) > 0

    participant = Participant()
    participant.from_mapping(raw_data[0])

    assert participant.OrganisationId != ''
    
    if len(participant.AuthorisationServers) > 0:
        for server in participant.AuthorisationServers:
            assert server.OpenIDDiscoveryDocument != ''
    
