import pytest
import json  # Import the JSON module
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_complete_flow(client):
    """ Test the complete keyword extraction workflow. """
    text = 'Natural language processing enables computers to understand human language.'
    response = client.post('/extract_keywords', json={'text': text})
    assert response.status_code == 200
    keywords = json.loads(response.data).get('keywords')
    assert 'computers' in keywords
    assert 'understand' in keywords