import os
import json

def read_json(path):
    """reads and provodes the json file content as python dictionary"""
    with open(path, "r") as f:
        content = f.read()
        # print(content)
        data = json.loads(content)
        return dict(data)