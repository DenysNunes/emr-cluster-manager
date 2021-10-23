import os, sys
import pytest

workspace_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(workspace_path))
path = os.path.dirname(__file__)

import main
from models import base as bs
from metastore import database as db

bs.Base.metadata.drop_all(bind=db.engine, tables=[bs.Cluster.__table__, bs.Instance.__table__])

def test_database_default_integrity():
    db.init_database()    
    assert main.session.query(bs.Cluster).count() > 0
    assert main.session.query(bs.Instance).count() > 0