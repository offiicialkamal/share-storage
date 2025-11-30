import os
import json

def read_json(path):
    f = open(path, "r")
    data = json.laod(f)
    f.close()
    return data
    
