import os, sys
import pytest

workspace_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(workspace_path))
path = os.path.dirname(__file__)

import main
from models import base as bs
from fastapi.testclient import TestClient
from metastore import database as db

client = TestClient(main.app)


def test_instances_api():
    response = client.get("/instances/")
    assert response.status_code == 200


def test_clusters_api():
    response = client.get("/clusters/")
    assert response.status_code == 200

