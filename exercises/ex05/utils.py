"""A group of utility functions that will be unit tested"""

__author__ = "730650836"


def only_evens(list_1: list[int]) -> list[int]:
    """Finds only the even ints and copies them to a new list"""
    idx = 0
    list_2: list[int] = []
    # Setting an empty list
    while idx < len(list_1):
        if list_1[idx] % 2 == 0:
            # If the remainder of dividing by 2 = 0 then it is even
            list_2.append(list_1[idx])
            # Adds the even numbers to a new list to not mutate the original list
        idx += 1
    return list_2


def sub(list_1: list[int], int_1: int, int_2: int) -> list[int]:
    """Creates a sub list of the ints between the starting and ending indexes"""
    list_2: list[int] = []
    if int_1 < 0:
        int_1 = 0
    if int_2 > len(list_1):
        int_2 = len(list_1)
    # First 2 conditionals are setting index parameters correct if the first is too low or the second is too high
    if len(list_1) == 0:
        return list_2
    if int_1 >= len(list_1):
        return list_2
    if int_2 <= 0:
        return list_2
    # Last 3 conditionals tell the function to return an empty list as the input index isn't available
    while int_1 < int_2:
        list_2.append(list_1[int_1])
        # Creates the new list with the ints in the range above
        int_1 += 1
    return list_2


def add_at_index(list_1: list[int], int_1: int, int_2: int) -> None:
    """Adds the first int at the index of the second int. Moves the rest of the list over one"""
    if int_2 > len(list_1):
        raise IndexError("Index is out of bounds for the input list")
    if int_2 < 0:
        raise IndexError("Index is out of bounds for the input list")
    # Two IndexError statements for the second int being too high or too low
    list_1.append(0)
    idx = len(list_1)
    # Adding a placeholder at the end so the while loop will work. Also setting idx = the length of the list and will count down as ints move over
    while idx > int_2:
        # Using this syntax to ensure all ints move before index reassignment
        list_1[idx - 1] = int(list_1[idx - 2])
        idx -= 1
        # Reassigning ints to one index higher and subtracting one from the idx to move through the list
    list_1[int_2] = int_1
    # List index reassignment in the desired index location
