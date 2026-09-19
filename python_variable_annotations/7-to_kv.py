#!/usr/bin/env python3
"""Module that provides a to_kv function."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of a string and the square of a number.

    Args:
        k: The string to include in the tuple.
        v: The int or float to square.

    Returns:
        A tuple containing k and the square of v as a float.
    """
    return (k, v ** 2)
