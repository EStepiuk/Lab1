import unittest
from model import Model


class TestModel(unittest.TestCase):
    def test_create(self):
        model = Model()
        self.assertIsNotNone(model.get_all_games());

    def test_add_result(self):
        model1 = Model()
        model2 = Model()
        self.assertEqual(model1.get_all_games(), model2.get_all_games())
        model2.add_result('test', 'test', 'test', 'test')
        self.assertNotEqual(model1.get_all_games(), model2.get_all_games())

    def test_get_by_team(self):
        model = Model()
        self.assertIsNotNone(model.get_by_team('MU'))
