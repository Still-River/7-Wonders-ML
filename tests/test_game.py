import unittest

from seven_wonders.Resources import ResourceOptions, ResourceOption
from seven_wonders.Science import Science
from seven_wonders.Card import Card
from seven_wonders.Deck import Deck
from seven_wonders.Player import Player
from seven_wonders.Game import Game

class TestGame(unittest.TestCase):
    def test_init(self):
        game = Game(num_players=7, seed=42)
        
        with self.subTest("Test Player Hand Size"):
            self.assertEqual(len(game.players[0].cards), 7)
            self.assertEqual(len(game.players[-1].cards), 7)

        with self.subTest("Test Player Hand Contents"):
            self.assertEqual(game.players[0].cards[0].name, 'Barracks')
            self.assertEqual(game.players[0].cards[-1].name, 'Theater')
            self.assertEqual(game.players[-1].cards[0].name, 'Tree Farm')
            self.assertEqual(game.players[-1].cards[-1].name, 'Altar')

if __name__ == '__main__':
    unittest.main()