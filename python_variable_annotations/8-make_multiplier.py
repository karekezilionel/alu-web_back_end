#!/usr/bin/env python3
"""Module that provides a make_multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier.

    Args:
        multiplier: The float to multiply by.

    Returns:
        A function that takes a float and returns its product
        with multiplier.
    """
    def multiply(n: float) -> float:
        """Multiply n by multiplier."""
        return n * multiplier

    return multiply
