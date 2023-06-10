from seven_wonders.Resources import ResourceOptions, ResourceOption
from seven_wonders.Science import Science
from seven_wonders.helpers import card_type_to_color

class Card():
    def __init__(self, name: str, min_players: int=3, age: int=1, type: str='none', victory_points: int=0,
                 resources: ResourceOptions=ResourceOptions(ResourceOption()),
                 cost: ResourceOptions=ResourceOptions(ResourceOption()),
                 shields: int=0, science: Science=Science()):
        self.name = name
        self.min_players = min_players
        self.age = age
        self.type = type
        self.victory_points = victory_points
        self.resources = resources
        self.cost = cost
        self.shields = shields
        self.science = science

    def __repr__(self):
        return f"Card(name={self.name!r}, min_players={self.min_players}, age={self.age}, type={self.type!r}, victory_points={self.victory_points}, resources={self.resources}, cost={self.cost}, shields={self.shields}, science={self.science})"

    def string_in_color(self, string):
        return f"{card_type_to_color(self.type)}{string}{card_type_to_color('reset')}"

    def important_attribute(self):
        match self.type:
            case 'raw_material' | 'manufactured_good':
                return f"Resources: {self.resources}"
            case 'civilian_structure':
                return f"Victory Points: {self.victory_points}"
            case 'scientific_structure':
                return f"Science: {self.science}"
            case 'military_structure':
                return f"Shields: {self.shields}"
            case _:
                pass