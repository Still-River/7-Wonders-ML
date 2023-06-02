from seven_wonders.Resources import ResourceOptions, ResourceOption
from seven_wonders.Science import Science
from seven_wonders.Card import Card
from seven_wonders.helpers import parse_string_to_resource, parse_string_to_science, parse_card_type

import pandas as pd

class Deck():
    def __init__(self, players: int=3):
        self.cards = []
        self.load_cards()

    def load_cards(self):
        df = pd.read_excel('resources/cards.xlsx')
        for card in df.itertuples():
            self.cards.append(Card(name=card.name, min_players=card.min_players, age=card.age, type=parse_card_type(card.type), victory_points=card.victory_points, resources=parse_string_to_resource(card.resources), cost=parse_string_to_resource(card.cost), shields=card.shields, science=parse_string_to_science(card.science)))