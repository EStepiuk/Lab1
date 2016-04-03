import pickle
from model import Model


def write(obj=Model().England, filename='../res/pickle_file.pickle'):
    with open(filename, 'wt') as f:
        pickle.dump(obj, f)


def read(filename='../res/pickle_file.pickle'):
    with open(filename, 'r') as f:
        return pickle.load(f)
