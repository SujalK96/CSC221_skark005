from random import randint

class Die():
    """A class representing a single eight-sided die (D8)."""
    
    def __init__(self, num_sides=8):
        """Initialize the die with 8 sides."""
        self.num_sides = num_sides
        
    def roll(self):
        """Roll the die and return a random value between 1 and 8."""
        return randint(1, self.num_sides)
