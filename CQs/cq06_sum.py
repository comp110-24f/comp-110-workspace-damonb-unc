"""Summing the elements of a list using different loops."""

__author__ = "730650836"


def w_sum(vals: list[float]) -> float:
    idx = 0
    x = 0.0
    y = 0.0
    while idx < len(vals):
        x = vals[idx]
        y = x + y
        idx += 1
    return y


def f_sum(vals: list[float]) -> float:
    y = 0.0
    for elem in vals:
        x = elem
        y = x + y
    return y


def f_range_sum(vals: list[float]) -> float:
    y = 0.0
    for idx in range(0, len(vals)):
        y = float(idx) + y
    return y
