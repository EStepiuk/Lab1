import yaml


def write(obj, filename='../res/yam_file.yaml'):
    with open(filename, 'wt') as f:
        yaml.dump(obj, f)


def read(filename='../res/yam_file.yaml'):
    with open(filename, 'r') as f:
        return yaml.load(f)
