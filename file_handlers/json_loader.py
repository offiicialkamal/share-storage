import os
import json

def read_json(path):
    """reads and provodes the json file content as python dictionary"""
    with open(path, "r") as f:
        data = json.laod(f.read())
        return dict(data)