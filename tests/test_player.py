from seven_wonders.Card import Card
from seven_wonders.Deck import Deck
from seven_wonders.Player import Player

import unittest
from io import StringIO
import sys
import re

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player()
        deck = Deck(num_players=3, seed=42)

        player.cards = deck[0][0:3]

    def test_display_hand(self):
        player = Player()
        deck = Deck(num_players=3, seed=42)

        player.cards = deck[0][3:9]
        player.cards.append(deck[2][3])

        with self.subTest("Test Display Hand"):
            captured_output = StringIO()
            sys.stdout = captured_output
            
            player.display_hand()

            printed_output = captured_output.getvalue()
            sys.stdout = sys.__stdout__
            printed_output = (remove_colors(printed_output.strip()))
            
            expected_output = "| Card Name |            Clay Pit            |       Baths       | West Trading Post |  Stockade  |     Apothecary     |          Loom          |      Strategist Guild       |\n|   Cost    |            [1 coin]            |     [1 stone]     |        []         |  [1 wood]  |    [1 textile]     |           []           | [1 stone, 2 ore, 1 textile] |\n|  Ability  | Resources: [1 clay] or [1 ore] | Victory Points: 3 |       None        | Shields: 1 | Science: 1 compass | Resources: [1 textile] |            None             |"
            
            self.assertEqual(printed_output, expected_output)

def remove_colors(text):
    # Remove escape sequences for colors
    pattern = re.compile(r'\033\[[0-9;]*m')
    return pattern.sub('', text)

if __name__ == '__main__':
    unittest.main()