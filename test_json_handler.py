# test_json_handler.py

"""
Module for testing the JsonHandler class with pytest.
"""

import pytest
from json_handler import JsonHandler  # assuming the class is in json_handler.py

def requirement(req_id):
    """
    A decorator to associate a test function with a requirement ID.
    """
    def decorator(function):
        function.requirement = req_id
        return function
    return decorator

@pytest.fixture
def json_handler():
    """
    Fixture to provide an instance of JsonHandler.
    """
    return JsonHandler()

@pytest.fixture
def temp_file(tmp_path):
    """
    Fixture to provide a temporary file path for testing.
    """
    return tmp_path / "test.json"

@requirement("REQ-101")
def test_read_json(json_handler, temp_file):
    """
    Test reading JSON data from a file.
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler, temp_file):
    """
    Test writing JSON data to a file.
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler):
    """
    Test checking for a key in JSON data.
    """
    data = {"test": "data"}
    assert json_handler.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler, temp_file):
    """
    Test updating JSON data in a file.
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    json_handler.update_json("test", "new data", temp_file)
    updated_data = json_handler.read_json(temp_file)
    assert updated_data["test"] == "new data"