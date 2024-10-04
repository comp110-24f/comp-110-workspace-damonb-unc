"""Practice with importing and scope - coordinates"""

__author__ = "730650836"


def get_coords(xs: str, ys: str) -> None:
    x_index = 0
    y_index = 0
    while x_index < len(xs):
        if y_index < len(ys):
            print("(" + str(xs[x_index]) + "," + str(ys[y_index]) + ")")
            y_index += 1
        else:
            x_index += 1
            y_index = 0
