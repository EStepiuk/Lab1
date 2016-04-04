import json


def write(obj, filename='../res/json_file.json'):
    with open(filename, 'wt') as f:
        json.dump(obj, f)


def read(filename='../res/json_file.json'):
    with open(filename, 'r') as f:
        return json.load(f)