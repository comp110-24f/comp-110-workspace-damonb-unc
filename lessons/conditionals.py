"""Practice with Conditionals"""


def less_than_10(num: int) -> None:
    """Tell me if num < 10"""
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")
    print("Have a nice day!")


(less_than_10(num=4))


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger"""

    if hungry:
        print("Eat some food")
    else:
        print("Do your homework")
    print("I'm proud of you")


should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> str:
    """Check if letter is first character of word"""
    if letter == word[0]:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
