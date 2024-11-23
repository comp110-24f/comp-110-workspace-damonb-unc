"""File to define Fish class."""

__author__ = "730650836"


class Fish:
    """Creates a class for Fish."""

    age: int

    def __init__(self):
        """Sets parameter for class to 0."""
        self.age = 0
        return None

    def one_day(self):
        """Simulates one day."""
        self.age += 1
        return None
