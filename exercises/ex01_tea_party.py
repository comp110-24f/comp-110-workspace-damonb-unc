"""Calculate the cost and number of tea bags and treats for a party"""

__author__ = "730650836"


def main_planner(guests: int) -> None:
    """Bring all the functions together"""
    """String notations plus call functions using guest parameter to match with other parameters"""
    print("A Cozy Tea Party for " + str(guests) + " People")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """The number of tea bags needed for the party"""
    return people * 2


def treats(people: int) -> int:
    """Compute the number of treats based on tea bags"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """compute the cost of the tea bags and the treats combined"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    """Make the program user friendly and more interactive"""
