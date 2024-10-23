__author__ = "730650836"


def find_and_remove_max(list_1: list[int]) -> int:
    idx = 0
    max: int = -1
    for elem in list_1:
        if elem > max:
            max = elem
    while idx < len(list_1):
        if list_1[idx] == max:
            list_1.pop(idx)
        else:
            idx += 1
    return max
