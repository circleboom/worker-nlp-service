import pytest
from flask import json
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """ Test the home/root route. """
    response = client.get('/')
    assert response.status_code == 200

def test_keyword_extraction(client):
    """ Test the keyword extraction API. """
    response = client.post('/extract_keywords', json={'text': 'Test the NLP service.'})
    data = json.loads(response.data)
    assert 'keywords' in data
    assert 'Test' in data['keywords']
    assert response.status_code == 200
