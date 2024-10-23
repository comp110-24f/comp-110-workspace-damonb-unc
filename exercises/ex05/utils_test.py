"""Testing the utility functions defined in the utils file"""

__author__ = "730650836"


from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_return() -> None:
    """Testing the return of only_evens_return"""
    nums: list[int] = [11, 12, 13, 13, 9, 10, 13]
    assert only_evens(nums) == [12, 10]


def test_only_evens_mutate() -> None:
    """Testing the mutation of only_evens_return"""
    nums: list[int] = [11, 12, 13, 13, 9, 10, 13]
    only_evens(nums)
    assert nums == [11, 12, 13, 13, 9, 10, 13]


def test_only_evens_edge() -> None:
    """Testing an abnormal situation with only_evens_return"""
    nums: list[int] = [11, 13, 13, 9, 7, 15, 19]
    assert only_evens(nums) == []


def test_sub_return() -> None:
    """Testing the return of sub"""
    nums: list[int] = [11, 12, 13, 13, 9, 10, 13]
    assert sub(nums, 2, 5) == [13, 13, 9]


def test_sub_mutate() -> None:
    """Testing the mutation of sub"""
    nums: list[int] = [11, 12, 13, 13, 9, 10, 13]
    sub(nums, 1, 4)
    assert nums == [11, 12, 13, 13, 9, 10, 13]


def test_sub_edge() -> None:
    """Testing an abnormal situation with sub"""
    nums: list[int] = []
    assert sub(nums, 3, 5) == []


def test_add_at_index_return() -> None:
    """Testing the return of add_at_index"""
    nums: list[int] = [11, 12, 13, 13, 9, 10, 13]
    assert add_at_index(nums, 5, 2) == None


def test_add_at_index_mutate() -> None:
    """Testing the mutation of add_at_index"""
    nums: list[int] = [11, 12, 13, 13, 9, 10, 13]
    add_at_index(nums, 8, 3)
    assert nums == [11, 12, 13, 8, 13, 9, 10, 13]


def test_add_at_index_edge() -> None:
    """Testing an abnormal situation with add_at_index"""
    nums: list[int] = [11, 12, 13, 13, 9, 10, 13]
    with pytest.raises(IndexError):
        add_at_index(nums, 11, 15)
