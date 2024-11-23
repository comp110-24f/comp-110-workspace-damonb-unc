"""Practice using dictionary functions in python"""

__author__ = "730650836"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Inverts the key and value pairs in a dictionary"""
    dict_2: dict[str, str] = {}
    # Setting an empty string
    for key in dict_1:
        # Checking if key is in the dictionary
        if dict_1[key] in dict_2:
            raise KeyError("Cannot invert because there would be identical keys!")
        else:
            a = dict_1[key]
            b = key
            dict_2[a] = b
            # Setting the key and value variables as local variables so they aren't lost
    return dict_2


def favorite_color(dict_1: dict[str, str]) -> str:
    """Finds the favorite color given a dictionary of people and their favorite colors"""
    color_count: dict[str, int] = {}
    for name in dict_1:
        a = dict_1[name]
        # Have to access the value variable in the dictionary
        if a in color_count:
            color_count[a] += 1
            # Adding to an existing color count
        else:
            color_count[a] = 1
            # Starting a new count if color isn't present
    max_color: str = ""
    count = 0
    for color in color_count:
        if color_count[color] > count:
            count = color_count[color]
            max_color = color
            # Looping through numbers to determine the most popular color using conditional
    return max_color


def count(list_1: list[str]) -> dict[str, int]:
    """Counts the number of unique values in a given list"""
    counts: dict[str, int] = {}
    for value in list_1:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
            # Looping through to see if value exists and if not, creates a new key to start counting
    return counts


def alphabetizer(list_1: list[str]) -> dict[str, list[str]]:
    """Groups words by their first letter"""
    name_list: dict[str, list[str]] = {}
    for name in list_1:
        first_letter = name[0]
        # Used to determine first letter to categorize
        if first_letter.lower() in name_list:
            # The .lower() is used to evaluate capital and lowercase letters
            name_list[first_letter].append(name)
            # Adding name to dictionary list
        else:
            name_list[first_letter.lower()] = [name]
    return name_list


def update_attendance(dict_1: dict[str, list[str]], weekday: str, student: str) -> None:
    """Creates a mutating dictionary that keeps track of attendance through the week"""
    if weekday in dict_1:
        if not student in dict_1[weekday]:
            dict_1[weekday].append(student)
    else:
        dict_1[weekday] = [student]
        # No looping needed as we are just looking at a singular pairing of values
        # Using the input dictionary to mutate rather than create a new dictionary
