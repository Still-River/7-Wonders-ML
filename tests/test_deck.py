import unittest

from seven_wonders.Resources import ResourceOptions, ResourceOption
from seven_wonders.Science import Science
from seven_wonders.Card import Card
from seven_wonders.Deck import Deck

class TestDeck(unittest.TestCase):
    def test_init(self):
        deck = Deck()
        cards = deck.cards

        first_card = cards[0]
        
        self.assertEqual(first_card.name, 'Lumber Yard')
        self.assertEqual(first_card.min_players, 3)
        self.assertEqual(first_card.age, 1)
        self.assertEqual(first_card.type, 'raw_material')
        self.assertEqual(first_card.victory_points, 0)
        self.assertEqual(first_card.resources, ResourceOptions(ResourceOption(wood=1)))
        self.assertEqual(first_card.cost, ResourceOptions(ResourceOption()))
        self.assertEqual(first_card.shields, 0)
        self.assertEqual(first_card.science, Science())

        another_card = cards[42]
        self.assertEqual(another_card.name, 'Guard Tower')
        self.assertEqual(another_card.min_players, 4)
        self.assertEqual(another_card.age, 1)
        self.assertEqual(another_card.type, 'military_structure')
        self.assertEqual(another_card.victory_points, 0)
        self.assertEqual(another_card.resources, ResourceOptions(ResourceOption()))
        self.assertEqual(another_card.cost, ResourceOptions(ResourceOption(clay=1)))
        self.assertEqual(another_card.shields, 1)
        self.assertEqual(another_card.science, Science())        

if __name__ == '__main__':
    unittest.main()