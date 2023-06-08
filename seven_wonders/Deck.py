from seven_wonders.Resources import ResourceOptions, ResourceOption
from seven_wonders.Science import Science
from seven_wonders.Card import Card
from seven_wonders.helpers import parse_string_to_resource, parse_string_to_science, parse_card_type

import random
import pandas as pd

class Deck():
    def __init__(self, num_players: int=3):
        self.cards = []
        self.num_players = num_players
        self.num_guild_cards = self.num_players + 2
        self.prepare_deck()

    def prepare_deck(self):
        self.load_cards()
        self.split_into_ages()
        self.shuffle()

    def load_cards(self):
        df = pd.read_excel('resources/cards.xlsx', engine='openpyxl')
        df = self.trim_deck_to_player_count(df)
        df = self.choose_guild_cards(df)
        for card in df.itertuples():
            self.cards.append(Card(name=card.name, min_players=card.min_players, age=card.age, type=parse_card_type(card.type), victory_points=card.victory_points, resources=parse_string_to_resource(card.resources), cost=parse_string_to_resource(card.cost), shields=card.shields, science=parse_string_to_science(card.science)))

    def trim_deck_to_player_count(self, df):
        df = df[df.min_players <= self.num_players]
        return df

    def choose_guild_cards(self, df):
        guild_cards = df[df.type == 'Guild']
        guild_cards = guild_cards.sample(n=self.num_guild_cards, replace=False)
        df = df[df.type != 'Guild']
        df = pd.concat([df, guild_cards])
        return df
    
    def split_into_ages(self):
        self.age1 = []
        self.age2 = []
        self.age3 = []
        for card in self.cards:
            if card.age == 1:
                self.age1.append(card)
            elif card.age == 2:
                self.age2.append(card)
            else:
                self.age3.append(card)

    def shuffle(self, seed=None):
        if seed:
            self.load_cards()
            self.split_into_ages()
            random.seed(seed)

        random.shuffle(self.age1)
        random.shuffle(self.age2)
        random.shuffle(self.age3)