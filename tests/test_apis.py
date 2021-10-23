from fastapi.testclient import TestClient
import os, sys

workspace_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(workspace_path))
path = os.path.dirname(__file__)
import main

client = TestClient(main.app)

def test_read_main():
    response = client.get("/instances/")
    assert response.status_code == 200