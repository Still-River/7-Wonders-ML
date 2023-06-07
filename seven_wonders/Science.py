class Science():
    def __init__(self, tablet: int=0, gear: int=0, compass: int=0):
        self.tablet = tablet
        self.gear = gear
        self.compass = compass

    def __add__(self, other):
        return Science(self.tablet + other.tablet,
                       self.gear + other.gear,
                       self.compass + other.compass)
    
    def __eq__(self, other):
        return self.tablet == other.tablet and \
               self.gear == other.gear and \
               self.compass == other.compass
    
    def __repr__(self):
        return f"Science(tablet={self.tablet}, gear={self.gear}, compass={self.compass})"
    
    def calculate_points(self):
        return self.tablet**2 + self.gear**2 + self.compass**2 + 7 * min(self.tablet, self.gear, self.compass)