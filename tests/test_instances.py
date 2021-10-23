import os, sys
import pytest

workspace_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(workspace_path))
path = os.path.dirname(__file__)

from metastore import instances as ins
from models.base import Instance


def test_instance_get_metastore():
    assert type(ins.get_metastore()) == list
    assert type(ins.get_metastore()[0]) == Instance
 
