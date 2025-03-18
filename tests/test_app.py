import os
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_convert_to_pdf(client):
    """Test file upload and PDF conversion"""
    data = {
        'files': (open("sample.txt", "rb"), "sample.txt")
    }
    response = client.post('/convert-to-pdf', data=data, content_type='multipart/form-data')
    
    assert response.status_code == 200
    assert response.content_type == 'application/pdf'
