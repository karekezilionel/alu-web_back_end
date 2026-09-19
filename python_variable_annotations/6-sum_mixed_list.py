#!/usr/bin/env python3
"""Module that provides a sum_mixed_list function."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of ints and floats.

    Args:
        mxd_lst: The list of ints and floats to sum.

    Returns:
        The sum of mxd_lst as a float.
    """
    return sum(mxd_lst)
