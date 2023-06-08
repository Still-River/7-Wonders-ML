import unittest

from seven_wonders.Resources import ResourceOptions, ResourceOption
from seven_wonders.Science import Science
from seven_wonders.Card import Card
from seven_wonders.Deck import Deck

class TestDeck(unittest.TestCase):
    def test_init(self):
        deck = Deck(num_players=7, seed=42)

        age1_card = deck[0][14]
        
        self.assertEqual(age1_card.name, 'Marketplace')
        self.assertEqual(age1_card.min_players, 6)
        self.assertEqual(age1_card.age, 1)
        self.assertEqual(age1_card.type, 'commercial_structure')
        self.assertEqual(age1_card.victory_points, 0)
        self.assertEqual(age1_card.resources, ResourceOptions(ResourceOption()))
        self.assertEqual(age1_card.cost, ResourceOptions(ResourceOption()))
        self.assertEqual(age1_card.shields, 0)
        self.assertEqual(age1_card.science, Science())

        age2_card = deck[1][9]
        self.assertEqual(age2_card.name, 'Quarry')
        self.assertEqual(age2_card.min_players, 4)
        self.assertEqual(age2_card.age, 2)
        self.assertEqual(age2_card.type, 'raw_material')
        self.assertEqual(age2_card.victory_points, 0)
        self.assertEqual(age2_card.resources, ResourceOptions(ResourceOption(stone=2)))
        self.assertEqual(age2_card.cost, ResourceOptions(ResourceOption(coin=1)))
        self.assertEqual(age2_card.shields, 0)
        self.assertEqual(age2_card.science, Science())

        age3_card = deck[2][10]

        self.assertEqual(age3_card.name, 'Arsenal')
        self.assertEqual(age3_card.min_players, 4)
        self.assertEqual(age3_card.age, 3)
        self.assertEqual(age3_card.type, 'military_structure')
        self.assertEqual(age3_card.victory_points, 0)
        self.assertEqual(age3_card.resources, ResourceOptions(ResourceOption()))
        self.assertEqual(age3_card.cost, ResourceOptions(ResourceOption(wood=2, ore=1, textile=1)))
        self.assertEqual(age3_card.shields, 3)
        self.assertEqual(age3_card.science, Science())

    def test_deck_size(self):
        for num_players in range(3, 8):
            deck = Deck(num_players=num_players)
            len_cards = len(deck[0]) + len(deck[1]) + len(deck[2])
            self.assertEqual(len_cards, 7 * num_players * 3)

    def test_guild_cards(self):
        for num_players in range(3, 8):
            deck = Deck(num_players=num_players)
            guild_cards = [card for card in deck[2] if card.type == 'guild']
            self.assertEqual(len(guild_cards), num_players + 2)

    def test_age_split(self):
        for num_players in range(3,8):
            deck = Deck(num_players=num_players)
            for age in deck:
                self.assertEqual(len(age), 7 * num_players)
            
    def test_shuffle(self):
        deck = Deck(num_players=7, seed=42)

        self.assertEqual(deck[0][0].name, 'Altar')
        self.assertEqual(deck[0][5].name, 'Apothecary')
        self.assertEqual(deck[1][0].name, 'Bazar')
        self.assertEqual(deck[1][15].name, 'School')
        self.assertEqual(deck[1][-1].name, 'Training Ground')
        self.assertEqual(deck[2][0].name, 'Circus')
        self.assertEqual(deck[2][-1].name, 'Lighthouse')

if __name__ == '__main__':
    unittest.main()