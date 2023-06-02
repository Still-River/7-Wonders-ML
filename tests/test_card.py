import unittest

from seven_wonders.Card import Card
from seven_wonders.Resources import ResourceOptions, ResourceOption
from seven_wonders.Science import Science

class TestCard(unittest.TestCase):
    def test_init(self):
        
        with self.subTest("Raw Material"):
            card = Card(name='Lumber Yard', min_players=3, age=1, type='raw_material', resources=ResourceOptions(ResourceOption(wood=1)))

            self.assertEqual(card.name, 'Lumber Yard')
            self.assertEqual(card.min_players, 3)
            self.assertEqual(card.age, 1)
            self.assertEqual(card.type, 'raw_material')
            self.assertEqual(card.victory_points, 0)
            self.assertEqual(card.resources, ResourceOptions(ResourceOption(wood=1)))
            self.assertEqual(card.cost, ResourceOptions(ResourceOption()))
            self.assertEqual(card.shileds, 0)
            self.assertEqual(card.science, Science())

        with self.subTest("Scientific Structure"):
            card = Card(name="Apothecary", min_players=3, age=1, type='scientific_structure', science=Science(tablet=1), cost=ResourceOptions(ResourceOption(textile=1)))

            self.assertEqual(card.name, 'Apothecary')
            self.assertEqual(card.min_players, 3)
            self.assertEqual(card.age, 1)
            self.assertEqual(card.type, 'scientific_structure')
            self.assertEqual(card.victory_points, 0)
            self.assertEqual(card.resources, ResourceOptions(ResourceOption()))
            self.assertEqual(card.cost, ResourceOptions(ResourceOption(textile=1)))
            self.assertEqual(card.shileds, 0)
            self.assertEqual(card.science, Science(tablet=1))

        with self.subTest("Civilian Structure"):
            card = Card(name="Pawnshop", min_players=4, age=1, type='civilian_structure', victory_points=3, cost=ResourceOptions(ResourceOption()))

            self.assertEqual(card.name, 'Pawnshop')
            self.assertEqual(card.min_players, 4)
            self.assertEqual(card.age, 1)
            self.assertEqual(card.type, 'civilian_structure')
            self.assertEqual(card.victory_points, 3)
            self.assertEqual(card.resources, ResourceOptions(ResourceOption()))
            self.assertEqual(card.cost, ResourceOptions(ResourceOption()))
            self.assertEqual(card.shileds, 0)
            self.assertEqual(card.science, Science())

        with self.subTest("Military Structure"):
            card = Card(name="Stockade", min_players=3, age=1, type='military_structure', shileds=1, cost=ResourceOptions(ResourceOption(wood=1)))

            self.assertEqual(card.name, 'Stockade')
            self.assertEqual(card.min_players, 3)
            self.assertEqual(card.age, 1)
            self.assertEqual(card.type, 'military_structure')
            self.assertEqual(card.victory_points, 0)
            self.assertEqual(card.resources, ResourceOptions(ResourceOption()))
            self.assertEqual(card.cost, ResourceOptions(ResourceOption(wood=1)))
            self.assertEqual(card.shileds, 1)
            self.assertEqual(card.science, Science())

if __name__ == '__main__':
    unittest.main()