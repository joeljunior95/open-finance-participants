import pytest
from flask import Flask

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    yield app.test_client()

def test_status_code(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_request(client):
    rv = client.get('/')
    assert b'<!DOCTYPE html' in rv.data == 200