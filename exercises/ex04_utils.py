"""Reverse engineering abstracts and concepts within python"""

__author__ = "730650836"


def all(list_1: list[int], int_1: int) -> bool:
    """Function to determine if all ints are the same as the input int"""
    idx = 0
    x = False  # setting false as predetermined condition and a number of conditionals will change to true
    while idx < len(list_1):
        if (
            int_1 == list_1[idx]
        ):  # conditional if the int = a specific index of the list
            x = True
        else:
            x = False
            idx = len(list_1)  # immediately exits loop if one index doesn't match
        idx += 1
    return x


def max(input: list[int]) -> int:
    """Determines the max int in a given list"""
    if len(input) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # returns value error in the case of 2 empty lists
    x: int = input[
        0
    ]  # sets the variable to the first int in the list as there may be negative inputs
    for elem in input:  # for in loop to loop through the list
        if elem > x:
            x = elem  # conditional to determine if the elem is the biggest num and redefining x if true
    return x


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if two lists are deeply equal to each other"""
    x = False
    idx = 0
    if len(list_1) != len(list_2):
        idx = len(
            list_1
        )  # sets idx = the while loop conditional to bypass loop if list lengths don't match
    while idx < len(
        list_1
    ):  # idx's match so only one needs to be checked for the conditional
        if (
            list_1[idx] == list_2[idx]
        ):  # checking each individual index for matching int
            x = True
        if list_1[idx] != list_2[idx]:  # immediately exits loop if given 1 mismatch
            idx = len(list_1)
            x = False
        idx += 1
    if list_1 == []:
        if list_2 == []:
            x = True  # if statement for if the 2 lists are matching empty lists
    return x


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Adds the content of the second list to the end of the forst list"""
    idx = 0
    while idx < len(list_2):
        list_1.append(list_2[idx])
        idx += 1  # loops through the second list and adds each int individually to the first list


# Resubmitting because I went over my last few EX submissions and changed the """""" into # for correct commenting
