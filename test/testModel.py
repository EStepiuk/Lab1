import unittest
from model import Model
import yaml

class TestModel(unittest.TestCase):
    def test_create(self):
        model = Model()
        with open('../res/yamtest.yaml','wt') as f:
            yaml.dump(model,f)

        with open('../res/yamtest.yaml','r') as f:
            teet = yaml.load(f)

        print(teet.get_by_team('MU'))
        print(model.get_team_items(model.get_all_games()[0]))

        self.assertEqual(model.get_by_team('MU'),teet.get_by_team('MU'))
