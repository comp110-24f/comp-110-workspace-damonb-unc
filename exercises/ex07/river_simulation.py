"""Simulates through time in the river given bear and fish populations."""

__author__ = "730650836"

from exercises.ex07.river import River

# Create a new River instance with 10 Fish and 2 Bears.
my_river = River(num_fish=10, num_bears=2)

# View the initial river status.
my_river.view_river()
