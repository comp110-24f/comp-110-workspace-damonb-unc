"""File to define Bear class."""

__author__ = "730650836"


class Bear:
    """Creates a class for Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Sets the parameters for class to 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulates one day."""
        self.age += 1
        # Decrease hunger score by 1 each day.
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Simulates bears eating fish."""
        # Increase hunger score by the number of fish eaten.
        self.hunger_score += num_fish
