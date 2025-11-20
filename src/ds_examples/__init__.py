"""Data Structures Examples package.

Provides minimal, readable implementations of common data structures
with accompanying tests and a simple CLI demonstration.
"""

__all__ = [
    "Stack",
    "Queue",
    "LinkedList",
    "BinaryTree",
]

from .stack import Stack
from .queue import Queue
from .linked_list import LinkedList
from .binary_tree import BinaryTree

__version__ = "0.1.0"
