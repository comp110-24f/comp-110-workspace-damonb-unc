"""A python knock-off wordle game!!"""

__author__ = "730650836"


def input_word() -> str:
    """Ask for a 5 letter word input"""
    word = str(input("Enter a 5-character word:"))
    if len(word) != 5:
        """If statement using length of word as conditional"""
        print("Error: Word must contain 5 characters.")
        exit()
        """prints an error message and exits entire function"""
    print("'" + word + "'")
    """prints back input word"""
    return word  # returns word variable for use in contains_char function


def input_letter() -> str:
    """Ask for a single character input"""
    letter = str(input("Enter a single character:"))
    if len(letter) != 1:
        """If statement using length of letter as conditional"""
        print("Error: Character must be a single character.")
        exit()
        """prints an error message and exits entire function"""
    print("'" + letter + "'")
    """prints back input letter"""
    return letter  # returns letter variable for use in contains_char function


def contains_char(word: str, letter: str) -> None:
    """Searching indices for letter match"""
    print("Searching for " + letter + " in " + word)
    x = 0  # sets local variable to 0 for counting matching indices
    if letter == word[0]:
        print(letter + " found at index 0")
        x += 1  # uses a local variable and adds to it when a match is found
    if letter == word[1]:
        print(letter + " found at index 1")
        x += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        x += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        x += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        x += 1
    """Uses multiple if statements to test if there is a letter match within a word"""
    if x == 0:
        print("No instances of " + letter + " found in " + word)
    elif x == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(x) + " instances of " + letter + " found in " + word)
    """if statements displaying # of matches and the  plurality of 'instance'"""


def main() -> None:
    """ties the 3 functions together"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    """makes this file able to run as a module"""
    main()
