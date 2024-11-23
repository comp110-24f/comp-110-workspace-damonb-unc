"""File to define River class."""

__author__ = "730650836"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Creates a class for River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears.
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of bears and fish."""
        # Remove fish older than 3 days.
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        # Remove bears older than 5 days.
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self):
        """Simulates bears eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                # Each bear eats 3 fish if there are at least 5 fish available.
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Checks hunger conditions of bears."""
        # Create a new list containing only bears with hunger_score >= 0.
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None

    def repopulate_fish(self):
        """Simulates repopulation of fish."""
        # Calculate the number of new fish based on existing pairs.
        num_new_fish = (len(self.fish) // 2) * 4
        # Add the new fish to the list.
        self.fish.extend(Fish() for _ in range(num_new_fish))
        return None

    def repopulate_bears(self):
        """Simulates repopulation of bears."""
        # Calculate the number of new bears based on existing pairs.
        num_new_bears = len(self.bears) // 2
        # Add the new bears to the list.
        self.bears.extend(Bear() for _ in range(num_new_bears))
        return None

    def view_river(self):
        """Visually shows time passage and population of bears and fish."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1.
        self.day += 1
        # Simulate one day for all Bears.
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish.
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating.
        self.bears_eating()
        # Remove hungry Bear's from River.
        self.check_hunger()
        # Remove old Fish and Bear's from River.
        self.check_ages()
        # Simulate Fish repopulation.
        self.repopulate_fish()
        # Simulate Bear repopulation.
        self.repopulate_bears()
        # Visualize River.
        self.view_river()

    def one_river_week(self):
        """Simulates a week in the river."""
        # Call one_river_day seven times to simulate a week.
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Simulates the removal of fish."""
        # Remove the first 'amount' fish from the list, if available.
        self.fish = self.fish[amount:]
