from seven_wonders.Deck import Deck
from seven_wonders.Player import Player

class Game():
    def __init__(self, num_players: int = 3, seed: int = None) -> None:
        self.num_players = num_players
        self.deck = Deck(num_players=self.num_players) if seed is None else Deck(num_players=self.num_players, seed=seed)
        self.players = [Player() for _ in range(self.num_players)]

        i = 1
        for player in self.players:
            player.talk(f"Hello! I'm player {i}.")
            i+=1

        print("Are all players ready?")

        i = 1
        for player in self.players:
            player.talk(f"Player {i}: Yes!")
            i+=1

        print("Great! Let's begin!")

        self.deal_cards(age=1)
        # while len(self.players[0].cards) > 1:
        #     self.players_turns()
        # self.deal_cards(age=2)
        # while len(self.players[0].cards) > 1:
        #     self.players_turns()
        # self.deal_cards(age=3)
        # while len(self.players[0].cards) > 1:
        #     self.players_turns()

    def deal_cards(self, age: int):
        for _ in range (7):
            for player in self.players:
                player.cards.append(self.deck[age-1].pop())

    # def players_turns(self):
    #     for player in self.players:
    #         player.player_action()

game = Game(num_players=3)