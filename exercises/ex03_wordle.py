"""Implementing an emojified version of wordle!"""

__author__ = "730650836"


def input_guess(secret_word_len: int) -> str:
    """Ask for a specific letter word input"""
    word = str(
        input(f"Enter a {secret_word_len} character word: ")
    )  # using f-string so any number secret word can be used
    while len(word) != secret_word_len:
        """while loop using length of word as conditional"""
        x = input(f"That wasn't {secret_word_len} chars! Try again: ")
        """prints an error message and restarts while function"""
        word = x  # resets word to new input so infinite loop won't occur
    print("'" + word + "'")
    """prints back input word"""
    return word  # returns word variable for use in contains_char function


def contains_char(secret_word: str, char_guess: str) -> bool:
    """function used for determining if a character is in a word"""
    assert (
        len(char_guess) == 1
    )  # creates an error message is not going by 1 char at a time
    idx = 0
    x = False  # automatically set to false until a match changes to true
    while idx < len(secret_word):
        if str(char_guess) == str(
            secret_word[idx]
        ):  # looped if statement to determine of the function is true or false
            x = True
        idx += 1
    return x


def emojified(guess: str, secret: str) -> str:
    """function used to display the emojis indicating letter matches and at which index"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    copy: str = ""  # empty string to add concatenation of emojis to
    while idx < len(secret):
        if (
            contains_char(secret_word=secret, char_guess=guess[idx]) == True
        ):  # setting contains_char function to work in this function within a conditional
            if guess[idx] == secret[idx]:
                copy += GREEN_BOX
            else:
                copy += YELLOW_BOX
        else:
            copy += WHITE_BOX
        idx += 1
    return copy


"""the copy variable is added to as the while loop evaluates each character within the guess word"""


def main(secret: str) -> None:
    """brings all the functions together and ties the user interface together"""
    idx = 1  # starting at 1 because there is no 'turn 0'
    guess: str = ""
    while idx <= 6:  # used <= because there are up to 6 turns, not less than
        print(f"=== Turn {idx}/6 ===")
        guess = input_guess(secret_word_len=len(secret))
        print(emojified(guess=guess, secret=secret))
        idx += 1
        if (
            guess == secret
        ):  # without using a break, I made a conditional that sets idx above the while loop conditional so it will end the game loop
            print(f"You won in {idx - 1}/6 turns!")
            idx = 7
    if not guess == secret:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
