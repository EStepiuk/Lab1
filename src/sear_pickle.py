import pickle

def write(obj, filename='../res/pickle_file.pickle'):
    with open(filename, 'wt') as f:
        pickle.dump(obj, f)


def read(filename='../res/pickle_file.pickle'):
    with open(filename, 'r') as f:
        return pickle.load(f)
