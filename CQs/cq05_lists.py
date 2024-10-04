"""Mutating functions."""

__author__ = "730650836"


def manual_append(a: list[int], num: int) -> None:
    a.append(num)


def double(a: list[int]) -> None:
    idx = 0
    while idx < len(a):
        a[idx] *= 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
