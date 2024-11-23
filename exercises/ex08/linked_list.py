"""Implementing algorithms to process a singly-linked list data structure."""

from __future__ import annotations

__author__ = "730650836"


class Node:
    """Represents a single node in a singly-linked list."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializes a Node in a singly-linked list."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list.
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
print(one)
print(str(courses))
print(courses)
# Be sure to get to here!


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"

    print(to_str(one))
    print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: When head is the last node.
    if head.next is None:
        return head.value
    else:
        # Recursive Case:
        rest: int = last(head.next)
        return rest


# print(last(one)).  # Expect to print 2.
print(last(courses))  # Expect to print 301.


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of the Node at the given index in a linked list."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns the maximum value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    if head.next is None:
        return head.value
    max_of_rest = max(head.next)
    return head.value if head.value > max_of_rest else max_of_rest


def linkify(items: list[int]) -> Node | None:
    """Converts a list of integers into a linked list."""
    if not items:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list where each value is scaled by a given factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))
