import pytest
import os, sys
import builtins

workspace_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(workspace_path))
path = os.path.dirname(__file__)

from metastore import instances as ins


def test_instance_set():
    path = 'tests/dbtest_inst.pickle'
    assert ins.set_metastore(path) != ""


def test_instance_get():
    path = 'tests/dbtest_inst.pickle'
    assert type(ins.get_metastore(path)) == dict