import sys
import os
import pytest
from flask import Flask

# Ensure the root directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from app import app  # Import the Flask app correctly

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_convert_to_pdf(client):
    """Test the PDF conversion API endpoint."""
    test_file_path = "sample.txt"

    # Create a temporary test file
    with open(test_file_path, "w") as f:
        f.write("This is a test file for PDF conversion.")

    # Open the file and send it in the request
    with open(test_file_path, "rb") as f:
        data = {'files': (f, "sample.txt")}
        response = client.post('/convert-to-pdf', data=data, content_type='multipart/form-data')

    # Assertions
    assert response.status_code == 200
    assert response.content_type == 'application/pdf'

    # Clean up the test file
    os.remove(test_file_path)
