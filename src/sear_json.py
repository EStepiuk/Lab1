import json
from model import Model


def write(obj=Model().England, filename='../res/json_file.json'):
    with open(filename, 'wt') as f:
        json.dump(obj, f)


def read(filename='../res/json_file.json'):
    with open(filename, 'r') as f:
        return json.load(f)