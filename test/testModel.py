import unittest
from model import Model
import yaml

class TestModel(unittest.TestCase):
    def test_create(self):
        model = Model()
        with open('../resource/yamtest.yaml','wt') as f:
            yaml.dump(model,f)

        with open('../resource/yamtest.yaml','r') as f:
            teet = yaml.load(f)

        print(teet.get_by_team('MU'))
