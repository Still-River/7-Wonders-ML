from seven_wonders.helpers import card_type_to_color

class Player():
    def __init__(self):
        print("Player created!")
        self.cards = []

    def talk(self, string):
        print(string)

    # def player_action(self):
    #     self.display_hand()
    #     x = input("What would you like to do?\n")
    #     print("You did something!")
    #     return x
        
    def display_hand(self):
        card_names = [card.string_in_color(card.name) for card in self.cards]
        card_costs = [card.string_in_color(card.cost) for card in self.cards]
        card_abilities = [card.string_in_color(card.important_attribute()) for card in self.cards]
        headers = ["Card Name"] + card_names
        values = ["Cost"] + card_costs
        abilities = ["Ability"] + card_abilities

        column_widths = [max(len(header), max(len(val), len(ability))) for header, val, ability in zip(headers, values, abilities)]

        for header, width in zip(headers, column_widths):
            print(f"| {header:^{width}} ", end="")
        print("|")
        for value, width in zip(values, column_widths):
            print(f"| {value:^{width}} ", end="")
        print("|")
        for ability, width in zip(abilities, column_widths):
            print(f"| {ability:^{width}} ", end="")
        print("|")
