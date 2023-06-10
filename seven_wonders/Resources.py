class ResourceOption():
    def __init__(self, wood: int=0, stone: int=0, clay: int=0, ore: int=0, glass: int=0, papyrus: int=0, textile: int=0, coin: int=0):
        self.wood = wood
        self.stone = stone
        self.clay = clay
        self.ore = ore
        self.glass = glass
        self.papyrus = papyrus
        self.textile = textile
        self.coin = coin

    def __repr__(self):
        return (f"ResourceOption(wood={self.wood}, stone={self.stone}, clay={self.clay}, "
                f"ore={self.ore}, glass={self.glass}, papyrus={self.papyrus}, "
                f"textile={self.textile}, coin={self.coin})")

    def __add__(self, other):
        if isinstance(other, ResourceOption):
            return ResourceOption(wood=self.wood + other.wood, stone=self.stone + other.stone,
                                  clay=self.clay + other.clay, ore=self.ore + other.ore,
                                  glass=self.glass + other.glass, papyrus=self.papyrus + other.papyrus,
                                  textile=self.textile + other.textile, coin=self.coin + other.coin)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, ResourceOption):
            return (self.wood == other.wood and self.stone == other.stone and
                    self.clay == other.clay and self.ore == other.ore and
                    self.glass == other.glass and self.papyrus == other.papyrus
                    and self.textile == other.textile and self.coin == other.coin)
        else:
            return NotImplemented
        
    def __str__(self):
        return ', '.join([f"{value} {resource}" for resource, value in self.__dict__.items() if value != 0])

class ResourceOptions():
    def __init__(self, *options: ResourceOption):
        self.options = options

    def __add__(self, other):
        if isinstance(other, ResourceOption):
            return ResourceOptions(*[option + other for option in self.options])
        elif isinstance(other, ResourceOptions):
            return ResourceOptions(*[option + other_option for option in self.options for other_option in other.options])
        else:
            return NotImplemented

    def __repr__(self):
        return f"ResourceOptions({', '.join([repr(option) for option in self.options])})"
    
    def __eq__(self, other):
        if isinstance(other, ResourceOptions):
            return all([option in other.options for option in self.options])
        else:
            return NotImplemented
        
    def __iter__(self):
        return iter(self.options)
    
    def __str__(self):
        return ' or '.join(["[" + str(option) + "]" for option in self.options])
    
if __name__ == '__main__':
    option1 = ResourceOptions(ResourceOption(wood=1))
    option2 = ResourceOptions(ResourceOption(wood=1), ResourceOption(ore=1))

    combined = option1 + option2
    print(combined)

    option3 = ResourceOptions(ResourceOption(stone=1), ResourceOption(clay=1))

    combined = option1 + option2 + option3
    print(combined)