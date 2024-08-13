import json
import os
from ..main import path
from classes import CustomOpen


def read_all_data(filename):
    """
    Read all data from JSON file
    """
    file_path = path + filename
    if os.path.getsize(file_path) > 0:
        with CustomOpen(file_path, "r") as file:
            return json.load(file)
    return {}


def write_data(filename, data):
    file_path = path + filename
    """
    Write data to JSON file
    """
    if os.path.exists(file_path):
        with CustomOpen(file_path, "w") as file:
            json.dump(data, file, indent=4)
            return True
