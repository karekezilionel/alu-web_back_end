#!/usr/bin/env python3
"""Module that provides a measure_runtime coroutine."""
import asyncio
import time
from importlib import import_module

async_comprehension = import_module(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Measure runtime of running async_comprehension four times.

    Returns:
        The total runtime in seconds.
    """
    start = time.perf_counter()
    async_tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*async_tasks)
    return time.perf_counter() - start
