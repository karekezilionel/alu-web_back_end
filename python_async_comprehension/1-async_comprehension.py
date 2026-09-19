#!/usr/bin/env python3
"""Module that provides an async_comprehension coroutine."""
from typing import List
from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random floats using an async comprehension.

    Returns:
        A list of 10 random floats from async_generator.
    """
    return [i async for i in async_generator()]
