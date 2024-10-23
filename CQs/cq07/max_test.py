__author__ = "730650836"

from CQs.cq07.find_max import find_and_remove_max


def test_find_max_1() -> None:
    nums: list[int] = [11, 12, 13, 13, 9, 10, 13]
    assert find_and_remove_max(nums) == 13


def test_mutate_list() -> None:
    nums: list[int] = [11, 12, 13, 13, 9, 10, 13]
    find_and_remove_max(nums)
    assert nums == [11, 12, 9, 10]


def test_edge_test() -> None:
    nums: list[int] = []
    assert find_and_remove_max(nums) == -1
