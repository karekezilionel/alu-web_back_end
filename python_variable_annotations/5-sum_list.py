#!/usr/bin/env python3
"""Module that provides a sum_list function."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats.

    Args:
        input_list: The list of floats to sum.

    Returns:
        The sum of input_list as a float.
    """
    return sum(input_list)
