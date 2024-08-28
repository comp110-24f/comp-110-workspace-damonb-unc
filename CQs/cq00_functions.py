"""My first challeng question in COMP110!"""

__author__ = "730650836"


def mimic(message: str) -> str:
    """Return message back"""
    return message


def main() -> None:
    """Print the result of calling mimic"""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
