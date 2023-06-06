import unittest

from seven_wonders.Resources import ResourceOptions, ResourceOption
from seven_wonders.Science import Science
from seven_wonders.Card import Card
from seven_wonders.Deck import Deck

class TestDeck(unittest.TestCase):
    def test_init(self):
        deck = Deck(num_players=7)
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

    def test_deck_size(self):
        for num_players in range(3, 8):
            deck = Deck(num_players=num_players)
            cards = deck.cards
            self.assertEqual(len(cards), 7 * num_players * 3)

    def test_guild_cards(self):
        for num_players in range(3, 8):
            deck = Deck(num_players=num_players)
            guild_cards = [card for card in deck.cards if card.type == 'guild']
            self.assertEqual(len(guild_cards), num_players + 2)

    def test_age_split(self):
        for num_players in range(3,8):
            deck = Deck(num_players=num_players)
            age1 = deck.age1
            age2 = deck.age2
            age3 = deck.age3
            self.assertEqual(len(age1), 7 * num_players)
            self.assertEqual(len(age2), 7 * num_players)
            self.assertEqual(len(age3), 7 * num_players)
            

if __name__ == '__main__':
    unittest.main()